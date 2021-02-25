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
#print (os.getcwdb())

oFilePath = 'brain\\ex\\temp\\'+sys.argv[1] + '_output.txt'
iFilePath = 'brain\\ex\\temp\\'+sys.argv[1] + '_input.txt'

print(os.getpid());
i=0
while True:
    if i>10:
        outputFile = open(oFilePath, "w")
        outputFile.write('#~50')
        outputFile.close()
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