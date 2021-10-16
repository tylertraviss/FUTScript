#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:18:59 2021

@author: tylertravis
"""

import random

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
        
    def randomlyGeneratedPlayer(self):
        self.league = random.choice(["ACAA", "AUS", "RSEQ", "OUA East", "OUA West","CW West", "MLS", "CPL"])
        self.country = random.choice(["Canada", "USA"])
        self.firstname = random.choice(["Nolan","Lewis","Josh","Tyler", "Evan", "Marco", "Joseph", "Rick", "Morty", "Carman", "Will", "Cole", "Brandon", "Declan", "Scout", "Abdul", "Lee", "Mahommod"])
        self.lastname = random.choice(["Nolan","Barnfather","Bell","Comeau", "Couturier", "Court", "Wood", "Ellick", "Chamberlin", "Shaw", "De Gea", "Cangli", "McLovin"])
        self.fullname = self.firstname + " " + self.lastname
        self.position = random.choice(["GK", "LB", "CB", "RB", "CM", "CM", "CM", "LW", "ST", "RW"])
        self.otherpositions = []
        self.rating = random.randint(75, 90)
        
    def playerInfo(self):
        print("")
        print("Player Info for: {}".format(self.fullname))
        print("League:", self.league)
        print("Country:", self.country)
        print("Position:",self.position)
        print("Ratings:", self.rating)
        

