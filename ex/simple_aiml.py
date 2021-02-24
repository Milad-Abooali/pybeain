#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiml
import time

airob = aiml.Kernel()
airob.learn("std-startup.xml")
airob.respond("LOAD AIML")

lastInput = ''
while True:
    inputFile  = open('temp/input.txt', 'r')
    inputLines = inputFile.readline()
    if lastInput!=inputLines:
        lastInput = inputLines
        outputFile = open('temp/output.txt', "w")
        print (inputLines)
        output = airob.respond(inputLines)
        print ('res:'+output)
        outputFile.write(output)
        outputFile.write("\n")
        outputFile.close()
        time.sleep(3)
    print ('...')
    time.sleep(2)
    inputFile.close()

