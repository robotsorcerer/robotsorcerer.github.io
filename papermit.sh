#!/bin/bash

# commits kinecontrol and model and other working papers

cd downloads/Papers
#pdftk ~/Documents/Papers/SRS/Continuum/kinecontrol/kinecontrol.pdf output kinecontrol.pdf  user_pw semaphore


cp ~/Documents/Papers/SRS/Continuum/kinecontrol/kinecontrol.pdf kinecontrol.pdf

cp ~/Documents/Papers/SRS/Continuum/model/model.pdf ContinuumI.pdf

cd ../../

commit
