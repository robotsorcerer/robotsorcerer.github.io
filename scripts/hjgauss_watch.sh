#!/usr/bin/env zsh
# Poll ~/Documents/Papers/Presentations/HJGauss for .md changes, regenerate
# marp html/pdf, copy into blog/downloads/Papers, commit and push.

set -o pipefail

SRC_DIR="$HOME/Documents/Papers/Presentations/HJGauss"
BLOG_DIR="$HOME/Documents/blog"
DEST_DIR="$BLOG_DIR/downloads/Papers"
LOG_FILE="$BLOG_DIR/scripts/hjgauss_watch.log"
STATE_FILE="$BLOG_DIR/scripts/.hjgauss_watch_state"

export PATH="$HOME/.nvm/versions/node/v24.16.0/bin:$PATH"

log() {
  print -r -- "$(date '+%Y-%m-%d %H:%M:%S') $*" >> "$LOG_FILE"
}

md_fingerprint() {
  # Concatenate mtimes+sizes of all .md files in SRC_DIR (non-recursive)
  find "$SRC_DIR" -maxdepth 1 -iname "*.md" -exec stat -f "%N %m %z" {} \; 2>/dev/null | sort
}

log "watcher started, pid=$$"

prev_fp="$(md_fingerprint)"

while true; do
  sleep 20
  cur_fp="$(md_fingerprint)"
  if [[ "$cur_fp" != "$prev_fp" ]]; then
    log "change detected in .md files, waiting 90s for dump to settle..."
    sleep 90
    # re-check it settled (no further change in that window)
    settle_fp="$(md_fingerprint)"
    if [[ "$settle_fp" != "$(md_fingerprint)" ]]; then
      log "still changing, waiting another 60s..."
      sleep 60
    fi

    log "running marp (html + pdf) on $SRC_DIR"
    ( cd "$SRC_DIR" && marp --allow-local-files . ) >> "$LOG_FILE" 2>&1
    ( cd "$SRC_DIR" && marp --allow-local-files --pdf . ) >> "$LOG_FILE" 2>&1

    log "copying generated html/pdf into $DEST_DIR"
    # src_basename:dest_basename pairs; extension (html/pdf/md) is preserved per pair
    typeset -a mappings
    mappings=(
      "hjgauss_talk:hjgauss_talk"
      "hjgauss_talk:hjgauss_slides"
      "hjgauss_full_expo:hjgauss_full_expo"
      "amfs:hjgauss_mapf_talk"
      "amfs:hjgauss_mapf_slides"
    )
    for pair in "${mappings[@]}"; do
      src_base="${pair%%:*}"
      dest_base="${pair##*:}"
      for ext in html pdf md; do
        # only pdf gets the "_slides"/"_mapf_slides" alias names; html/md keep the talk-style name
        if [[ "$dest_base" == "hjgauss_slides" || "$dest_base" == "hjgauss_mapf_slides" ]] && [[ "$ext" != "pdf" ]]; then
          continue
        fi
        f="$SRC_DIR/$src_base.$ext"
        if [[ -f "$f" ]]; then
          cp -f "$f" "$DEST_DIR/$dest_base.$ext"
          log "  copied $src_base.$ext -> $dest_base.$ext"
        fi
      done
    done

    # Special rule: amfs.pdf (the MAPF/AMFS deck) copied as hjgauss_mapf.pdf
    if [[ -f "$SRC_DIR/amfs.pdf" ]]; then
      cp -f "$SRC_DIR/amfs.pdf" "$DEST_DIR/hjgauss_mapf.pdf"
      log "  copied amfs.pdf -> hjgauss_mapf.pdf"
    fi

    log "building jekyll site to sanity-check"
    ( cd "$BLOG_DIR" && bundle exec jekyll build --destination /tmp/_hjgauss_watch_build ) >> "$LOG_FILE" 2>&1

    log "git add/commit/push"
    ( cd "$BLOG_DIR" && git add downloads/Papers/hjgauss_talk.html downloads/Papers/hjgauss_talk.md \
        downloads/Papers/hjgauss_full_expo.html downloads/Papers/hjgauss_full_expo.md downloads/Papers/hjgauss_full_expo.pdf \
        downloads/Papers/hjgauss_mapf_talk.html downloads/Papers/hjgauss_mapf_talk.md \
        downloads/Papers/hjgauss_mapf.pdf downloads/Papers/hjgauss_slides.pdf downloads/Papers/hjgauss_mapf_slides.pdf \
        2>/dev/null ) >> "$LOG_FILE" 2>&1

    if ! ( cd "$BLOG_DIR" && git diff --cached --quiet ); then
      ( cd "$BLOG_DIR" && git commit -m "Auto-sync HJGauss slides/exposition from Presentations source" ) >> "$LOG_FILE" 2>&1
      ( cd "$BLOG_DIR" && git push origin master ) >> "$LOG_FILE" 2>&1
      log "committed and pushed"
    else
      log "no staged changes after copy, skipping commit"
    fi

    prev_fp="$(md_fingerprint)"
  else
    prev_fp="$cur_fp"
  fi
done
