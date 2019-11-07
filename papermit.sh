#!/bin/bash

# commits kinecontrol and model and other working papers

pdftk ../Papers/SRS/Continuum/kinecontrol/kinecontrol.pdf output  downloads/Papers/kinecontrol.pdf  user_pw semaphore

pdftk ../Papers/SRS/Continuum/model/model.pdf output downloads/Papers/ContinuumI.pdf

commit
