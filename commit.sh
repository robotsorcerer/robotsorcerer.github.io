#!/bin/bash

# commits a change
git add --all;

echo "please enter the commit message followed by [enter]: "

read msg

git commit -m "$msg"

git push -u origin master

