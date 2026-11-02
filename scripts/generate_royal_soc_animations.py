#!/usr/bin/env python3
"""Render Royal Society animations from the selected native solver snapshots.

Example: /usr/bin/python3.10 scripts/generate_royal_soc_animations.py --source
  /path/to/levelsetpy/monte_carlo/results/multidimensional
Only saved snapshots are displayed; frames are not interpolated in time.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.interpolate import RegularGridInterpolator


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render(source, output, selection, case, stem, title, extent, labels):
    config = selection[case]
    suffix = '_fd' if config.get('method') == 'fd' else ''
    run = f"{case}_full_{config['n']}_{config['steps']}_L6_c0.2{suffix}"
    archive = source / (run + '.npz')
    record = json.loads(archive.with_suffix('.json').read_text())
    digest = sha256(archive)
    if record.get('archive_sha256') and record['archive_sha256'] != digest:
        raise ValueError(f'Native archive digest mismatch: {run}')
    frames, times = [], []
    axis = np.linspace(-extent, extent, 161)
    X, Y = np.meshgrid(axis, axis, indexing='xy')
    with np.load(archive) as data:
        axes = tuple(data[f'axis_{i}'] for i in range(len(record['shape'])))
        snapshots = sorted((float(k[2:]), k) for k in data.files if k.startswith('t_'))
        for time, key in snapshots:
            queries = np.c_[X.ravel(), Y.ravel()]
            if len(axes) == 3:
                queries = np.c_[queries, np.zeros(X.size)]
            V = RegularGridInterpolator(axes, data[key], bounds_error=True)(queries).reshape(X.shape)
            if not np.isfinite(V).all():
                raise ValueError(f'Nonfinite slice: {run}/{key}')
            fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=100)
            fig.subplots_adjust(left=.13, right=.84, bottom=.16, top=.79)
            im = ax.contourf(X, Y, V, levels=np.linspace(-1, 1, 25), cmap='RdBu_r', extend='both')
            if V.min() < 0 < V.max():
                ax.contour(X, Y, V, levels=[0], colors='black', linewidths=1.5)
            ax.set(xlim=(-extent, extent), ylim=(-extent, extent), aspect='equal',
                   xlabel=labels[0], ylabel=labels[1])
            fig.suptitle(title, fontsize=15, y=.96)
            subtitle = 'Full residual' + ('; heading = 0 rad' if len(axes) == 3 else '')
            ax.set_title(f'{subtitle}\nElapsed horizon: {time:g}', fontsize=11, pad=10)
            fig.colorbar(im, cax=fig.add_axes([.87, .20, .025, .52]), label='Value', ticks=[-1, 0, 1])
            fig.text(.5, .025, 'Dimensionless quantities; black contour: value = 0', ha='center', fontsize=9)
            with io.BytesIO() as buffer:
                fig.savefig(buffer, format='png')
                buffer.seek(0)
                frames.append(Image.open(buffer).convert('RGB').copy())
            plt.close(fig)
            times.append(time)
    if len(frames) < 2:
        raise ValueError(f'Insufficient saved snapshots: {run}')
    gif = output / (stem + '.gif')
    frames[0].save(gif, save_all=True, append_images=frames[1:], loop=0,
                   duration=[350] * (len(frames) - 1) + [1200], optimize=False,
                   disposal=2)
    frames[-1].save(output / (stem + '_poster.png'))
    return dict(case=case, run=run, archive_sha256=digest,
                source_digests=record['source_digests'], saved_times=times,
                slice_heading=0 if len(axes) == 3 else None,
                window=[[-extent, extent], [-extent, extent]],
                slice_grid=[161, 161], gif_sha256=sha256(gif),
                interpretation=record['interpretation'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).resolve().parents[1] / 'downloads/Papers/assets/anim')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    selection_path = args.source / 'selection.json'
    selection = json.loads(selection_path.read_text())
    records = []
    for case, stem, title, extent, labels in [
        ('murmuration', 'roysoc_murmuration', 'Starling-inspired model: value evolution', 3,
         ('Relative position x₁', 'Relative position x₂')),
        ('double_integrator', 'roysoc_double_integrator', 'Double integrator: value evolution', 2,
         ('Position', 'Velocity')),
    ]:
        records.append(render(args.source, args.output, selection, case, stem, title, extent, labels))
    manifest = dict(selection_sha256=sha256(selection_path), animations=records,
                    temporal_interpolation=False,
                    note='Finite-grid fixed-horizon values; no trajectory or safety certificate.')
    (args.output / 'roysoc_animations.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Rendered two animations and posters from selected native archives.')


if __name__ == '__main__':
    main()
