#!/bin/bash

rm downloads/cv/resume.pdf

pdftk ~/Documents/Grants/cv/acad_cv.pdf output downloads/cv/resume.pdf  user_pw semaphore

commit
