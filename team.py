#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:04:40 2021

@author: tylertravis
"""

class Team():
    
    def __init__(self):
        self.clubname = "Default FC"
        self.chemistry = 0
        
        self.currentGK = 0
        self.currentLB = 0
        self.currentCB1 = 0
        self.currentCB2 = 0
        self.currentRB = 0
        self.currentCM1 = 0
        self.currentCM2 = 0
        self.currentCM3 = 0
        self.currentLW = 0
        self.currentST = 0
        self.currentRW = 0
        
        self.sub1 = 0
        self.sub2 = 0
        self.sub3 = 0
        self.sub4 = 0
        self.sub5 = 0
        
        self.squadlist = []
        
    def changeCardintoPosition(self, player, position):
        """
        Player goes into squad position
        """
        
        if (position == "GK"):
            self.currentGK = player
        
        elif (position == "LB"):
            self.currentLB = player
        
        elif (position == "CB1"):
            self.currentCB1 = player
            
        elif (position == "CB2"):
            self.currentCB2 = player
    
        elif (position == "RB"):
            self.currentRB = player

        elif (position == "CM1"):
            self.currentCM1 = player
        
        elif (position == "CM2"):
            self.currentCM2 = player
        
        elif (position == "CM3"):
            self.currentCM3 = player
            
        elif (position == "LW"):
            self.currentLW = player
    
        elif (position == "ST"):
            self.currentST = player
            
        elif (position == "RW"):
            self.currentRW = player
            
        elif (position == "sub1"):
            self.sub1 == player
            
        elif (position == "sub2"):
            self.sub2 == player
            
        elif (position == "sub3"):
            self.sub3 == player
            
        elif (position == "sub4"):
            self.sub4 == player
            
        elif (position == "sub5"):
            self.sub5 == player
            
    def printCurrentLine(self):
        print("")
        print("Starting Roster")
        print("GK: {}".format(self.currentGK.fullname))
        print("LB: {}".format(self.currentLB))
        print("CB1: {}".format(self.currentCB1))
        print("CB2: {}".format(self.currentCB2))
        print("RB: {}".format(self.currentRB))
        print("CM1: {}".format(self.currentCM1))
        print("CM2: {}".format(self.currentCM2))
        print("CM3: {}".format(self.currentCM3))
        print("LW: {}".format(self.currentLW))
        print("ST: {}".format(self.currentST.fullname))
        print("RW: {}".format(self.currentRW))
        print("")
        print("Subs:", self.sub1, self.sub2, self.sub3, self.sub4, self.sub5)

            
