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

# Function to List a "Card"

def displayPlayerCard(setx, sety, player):
    """
    Parameters
    ----------
    setx : int
        where you want x to be
    sety : int
        where you want y to be
    player : Player()
        The specific player we want to access in display

    Returns
    -------
    NA

    """
    
    # Eventually adjust color to overall.
    lbl = Label(window, text =  "("+str(player.rating) + ")", fg = 'black', justify = CENTER) 
    lbl.place(x=setx-35, y = sety)    
    
    lbl = Label(window, text=player.fullname, fg = 'black', justify = CENTER)
    lbl.place(x=setx, y = sety)
    lbl = Label(window, text = player.league, fg = 'black', justify = CENTER) 
    lbl.place(x=setx, y = sety+20)
    lbl = Label(window, text = player.country, fg = 'black', justify = CENTER) 
    lbl.place(x=setx, y = sety+40)
    
# Function for each menu button

def clickMain():
    print("Main Clicked")
    currentmenu = "Main"
    
def clickPlay():
    print("Play Clicked")
    currentmenu = "Play"
        
def clickRoster():
    print("Roster Clicked")
    currentmenu = "Roster"
    
    lbl = Label(window, text="Current Roster", fg = 'black')
    lbl.place(x=100, y = 45)
    
    # Displaying Roster
    
    displayPlayerCard(440, 500, teamA.currentGK) # GK
    
    # Back Line Displayed
    
    displayPlayerCard(200, 400, teamA.currentLB)
    displayPlayerCard(370, 400, teamA.currentCB1)
    displayPlayerCard(540, 400, teamA.currentCB2)
    displayPlayerCard(710, 400, teamA.currentRB)
    
    # Midfield
    
    displayPlayerCard(300, 300, teamA.currentCM1)
    displayPlayerCard(300+170, 300, teamA.currentCM2)
    displayPlayerCard(300+170+170, 300, teamA.currentCM3)
    
    # Strikers
    
    displayPlayerCard(200, 200, teamA.currentLW)
    displayPlayerCard(710, 200, teamA.currentRW)
    displayPlayerCard((200 + 710)/2, 175, teamA.currentST)
    
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

