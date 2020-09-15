#!/bin/bash

rm downloads/cv/resume.pdf

pdftk ~/Documents/Grants/cv/resume.pdf output downloads/cv/resume.pdf  user_pw semaphore

commit
