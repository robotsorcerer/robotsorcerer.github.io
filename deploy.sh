#! /bin/sh

bundle exec jekyll build -- trace --incremental;
bundle exec jekyll serve --trace --incremental

