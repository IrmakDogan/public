# -*- encoding: UTF-8 -*-

import sys
from naoqi import ALProxy
import time
import almath

def main(robotIP):
    PORT = 9559

    try:
        motionProxy = ALProxy("ALMotion","192.168.0.118", 9559)
    except Exception,e:
        print "Could not create proxy to ALMotion"
        print "Error was: ",e
        sys.exit(1)

    time.sleep(3.0)
    motionProxy.setStiffnesses("Head", 1.0)

    # Simple command for the HeadYaw joint at 10% max speed
    names            = "HeadPitch"
    angles           = 0.36477381367
    fractionMaxSpeed = 0.05
    motionProxy.setAngles(names,angles,fractionMaxSpeed)
    
    time.sleep(2.0)
    
    names            = "HeadPitch"
    angles           = -0.033161255788
    fractionMaxSpeed = 0.05
    motionProxy.setAngles(names,angles,fractionMaxSpeed)


    time.sleep(2.0)
    
    names            = "HeadPitch"
    angles           = 0.36477381367
    fractionMaxSpeed = 0.05
    motionProxy.setAngles(names,angles,fractionMaxSpeed)
    
    time.sleep(2.0)

if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print "Usage python almotion_controllingjoints.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)

