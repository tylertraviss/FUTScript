#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 23:01:46 2021

@author: tylertravis
"""

from team import *

# Testing 

playerA = Player()
playerA.randomGeneration()
#playerA.playerInfo()

teamA = Team()
teamA.changeCardintoPosition(playerA, "ST")

teamA.populateRoster()
teamA.printCurrentLine()

teamA.printRoster()