#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import aiml

alice = aiml.Kernel()
alice.learn("std-startup.xml")
alice.respond("LOAD AIML")

while True:
   print (alice.respond(input("> ")))
   