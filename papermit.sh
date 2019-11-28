#!/bin/bash

# commits kinecontrol and model and other working papers

cd downloads/Papers

#pdftk ~/Documents/Papers/SRS/Continuum/kinecontrol/kinecontrol.pdf output kinecontrol.pdf  user_pw semaphore
#
#pdftk ~/Documents/Papers/SRS/Springer2019/springer19.pdf output Springer19.pdf user_pw spring_it
#
#pdftk ~/Documents/Papers/SRS/Continuum/model/model.pdf output ContinuumI.pdf user_pw continua
#
cp ~/Documents/Papers/SRS/Continuum/kinecontrol/kinecontrol.pdf kinecontrol.pdf  
cp ~/Documents/Papers/SRS/Springer2019/springer19.pdf Springer19.pdf 

cp ~/Documents/Papers/SRS/Continuum/model/model.pdf ContinuumI.pdf



cd ../../

commit
