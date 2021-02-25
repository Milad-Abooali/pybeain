#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import aiml
import time

airob = aiml.Kernel()
airob.learn("brain\\ex\\std-startup.xml")
airob.respond("LOAD AIML")

lastInput = ''

oFilePath = 'brain\\ex\\temp\\'+sys.argv[1] + '\\response.log'
iFilePath = 'brain\\ex\\temp\\'+sys.argv[1] + '\\input.log'

pidFilePath = 'brain\\ex\\temp\\'+sys.argv[1] + '\\pid.log'
outputFile = open(pidFilePath, "w")
outputFile.write(os.getpid())
outputFile.close()

i=0
while True:
    if i>1500:
        os.remove(pidFilePath)
        break
    else:
        inputFile  = open(iFilePath, 'r')
        inputLines = inputFile.readline()
        if lastInput!=inputLines:
            i=0
            lastInput = inputLines
            outputFile = open(oFilePath, "w")
            outputFile.write(airob.respond(inputLines))
            outputFile.close()
            time.sleep(3)
        else:
            i = i+1
        inputFile.close()
        time.sleep(2)