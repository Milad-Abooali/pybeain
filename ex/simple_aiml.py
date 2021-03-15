#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import aiml
import time

airob = aiml.Kernel()
airob.learn("brain\\ex\\aiml-startup.xml")
airob.respond("LOAD AIML")

lastInput = ''

oFilePath = 'brain\\ex\\temp\\'+sys.argv[1] + '\\response.txt'
iFilePath = 'brain\\ex\\temp\\'+sys.argv[1] + '\\input.txt'

pidFilePath = 'brain\\ex\\temp\\'+sys.argv[1] + '\\pid.txt'
outputFile = open(pidFilePath, "w")
outputFile.write(str(os.getpid()))
outputFile.flush()
#outputFile.close()

i=0
while True:
    if i>180: # 180 : 3 min
        os.remove(pidFilePath)
        break
    else:
        inputFile  = open(iFilePath, 'r')
        inputLines = inputFile.readline()
        if lastInput!=inputLines:
            i=0
            lastInput = inputLines
            inputFile.close()
            outputFile = open(oFilePath, "w")
            outputFile.write(airob.respond(inputLines))
            outputFile.close()
            time.sleep(0.1)
        else:
            i = i+1
        time.sleep(0.1)