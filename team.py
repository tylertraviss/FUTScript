#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:04:40 2021

@author: tylertravis
"""

from player import *

rosterlength = 5

class Team():
    
    def __init__(self):
        
        self.clubname = "Default FC"
        self.roster = []
        self.chemistry = 0
        
        self.emptyPlayer = Player()
        
        self.currentGK = self.emptyPlayer
        self.currentLB = self.emptyPlayer
        self.currentCB1 = self.emptyPlayer
        self.currentCB2 = self.emptyPlayer
        self.currentRB = self.emptyPlayer
        self.currentCM1 = self.emptyPlayer
        self.currentCM2 = self.emptyPlayer
        self.currentCM3 = self.emptyPlayer
        self.currentLW = self.emptyPlayer
        self.currentST = self.emptyPlayer
        self.currentRW = self.emptyPlayer
        
        self.sub1 = self.emptyPlayer
        self.sub2 = self.emptyPlayer
        self.sub3 = self.emptyPlayer
        self.sub4 = self.emptyPlayer
        self.sub5 = self.emptyPlayer
        
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
        print("LB: {}".format(self.currentLB.fullname))
        print("CB1: {}".format(self.currentCB1.fullname))
        print("CB2: {}".format(self.currentCB2.fullname))
        print("RB: {}".format(self.currentRB.fullname))
        print("CM1: {}".format(self.currentCM1.fullname))
        print("CM2: {}".format(self.currentCM2.fullname))
        print("CM3: {}".format(self.currentCM3.fullname))
        print("LW: {}".format(self.currentLW.fullname))
        print("ST: {}".format(self.currentST.fullname))
        print("RW: {}".format(self.currentRW.fullname))
        print("")
        print("Subs:", self.sub1.fullname, self.sub2.fullname, self.sub3.fullname, self.sub4.fullname, self.sub5.fullname)

    def populateRoster(self):
        # generates roster
        for i in range(rosterlength):
            p = Player()
            p.randomlyGeneratedPlayer()
            self.roster.append(p)
            
    def printRoster(self):  
        # prints through all players on roster
        for i in range(rosterlength):
            self.roster[i].playerInfo()
            
    def findBest(self, position):
        """
        Takes in position, returns best player in roster of it.
        """
        
        listofplayers = []
        
        # Finds list of all players in that position.
        
        for i in range(rosterlength):
            
            # Is this player the position we want?
            if self.roster[i].position == position:
                listofplayers.append(self.roster[i])
           
        for i in range(len(listofplayers)):    
            print(listofplayers[i].position)    
           
        # Find max of ratings.
        
        playerratings = []
        
        for i in range(len(listofplayers)):
            playerratings.append(listofplayers[i].rating)
        
        print(playerratings)
        print(len(playerratings))
        
        if (len(playerratings) > 0):
        
            maxrating = max(playerratings)
            maxindex = playerratings.index(maxrating)
            return listofplayers[maxindex]
        
        else:
            print("No players in that position.")
            return None
        
        
        
    def autoCurrentLine(self):
        """
        Automatically selects your line, calls findbest.
        """
        pass
        
        # Picking Best Goalie
        
        
        
