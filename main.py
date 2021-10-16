#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 23:01:46 2021

@author: tylertravis
"""

from team import *
from tkinter import *




teamA = Team()
teamB = Team()

def tempTeams():
    teamA.clubname = "Riverview FC"
    teamB.clubname = "Moncton FC"
    
    positions = ["GK", "LB", "RB", "CB1", "CB2",
                 "CM1", "CM2", "CM3", "LW", "ST", "RW"]
    
    for x in positions:
        tempPlayer = Player()
        tempPlayer.randomlyGeneratedPlayer()
        teamA.changeCardintoPosition(tempPlayer, x)
        
        tempPlayer = Player()
        tempPlayer.randomlyGeneratedPlayer()
        teamB.changeCardintoPosition(tempPlayer, x)
            
# Testing 

tempTeams()
teamA.printCurrentLine()
teamB.printCurrentLine()

# --------------------------------------

# Start of User Interface

# Function for each menu button

def clickMain():
    print("Main Clicked")
    currentmenu = "Main"
    
def clickPlay():
    print("Play Clicked")
    currentmenu = "Play"
    
    #window.create_rectange(200,200,120,80) 
    
    
    
    
    
def clickRoster():
    print("Roster Clicked")
    currentmenu = "Roster"
    
def clickMarket():
    print("Market Clicked")
    currentmenu = "Market"
    
def clickExit():
    print("Exit Clicked")
    currentmenu = "Exit"

menus = ["Main", "Play", "Roster", "Market", "Exit"]
currentmenu = "Main"
commands = [clickMain, clickPlay, clickRoster, clickMarket, clickExit]


window=Tk()

yval = 175
indexof = 0

for x in menus:
    btn=Button(window, text=x, fg='black', command = commands[indexof])
    btn.place(x=20, y=yval)
    yval += 40
    indexof += 1

window.title('FUTSCRIPT')
window.geometry("900x600+10+10")




window.mainloop()

