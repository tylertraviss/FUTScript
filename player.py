#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:18:59 2021

@author: tylertravis
"""

class Player():
    
    """
    Creating Instance of Player
    """
    
    # Creating Empty Instance of Player    

    def __init__(self):    
        self.league = ""
        self.country = ""
        self.firstname = ""
        self.lastname = ""
        self.fullname = self.firstname + " " + self.lastname
        self.position = ""
        self.otherpositions = []
        
    def randomGeneration(self):
        self.league = "ACAA"
        self.country = "Canada"
        self.firstname = "Tyler"            
        self.lastname = "Travis"  
        self.fullname = self.firstname + " " + self.lastname 
        self.position = "CM"
        self.otherpositions = ["ST", "RW"]
        self.rating = 85
        
    def playerInfo(self):
        print("Player Info for: {}".format(self.fullname))
        print("League:", self.league)
        print("Country:", self.country)
        print("Position:",self.position)
        print("Ratings:", self.rating)
        

