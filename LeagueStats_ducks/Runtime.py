# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:18:10 2020

@author: Adam
"""
import csv

playerCSV = 'PlayerPools.csv'
playerInfo = {}
listTbl = []

class player:
    def __init__(self, ):
        pass
        
class playerinfo:
    @staticmethod
    def load_players(playerCSV):
        table = []
        with open(playerCSV, 'r') as objFile:
            reader = csv.DictReader(objFile)
            for row in reader:
                row.setdefault('Secondary', None)
                row.setdefault('R1 Team', None)
                row.setdefault('R2 Team', None)
                row.setdefault('R3 Team', None)
                row.setdefault('R4 Team', None)
#                lstRow = row.strip().split(',')
#                dictRow = {'ID': lstRow[0], 'Name': lstRow[1], 'Summoner': lstRow[2], 'Primary': lstRow[3]}
#                'Secondary': lstRow[4]
                table.append(row)
        return table
    
    @staticmethod
    def print_playerinfo(table):
        print('======= Players in Memory: =======')
        print('ID\tSummoner Name (Real Name)\n')
        for dictRow in table:
            print('{}\t{} ({})'.format(dictRow['Player Number'], dictRow['Real Name'], dictRow['Summoner Name']))
        print('======================================')

class IO:
    @staticmethod
    def print_menu():
        print('Menu\n\n[l] Load Player Info from file\n[i] Display Player Info Table\n[x] exit\n')
        
    @staticmethod
    def menu_choice():
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]:\n').lower().strip()
        return choice


listTbl = playerinfo.load_players(playerCSV)
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()

    if strChoice == 'x':
        break
    
    elif strChoice == 'l':
        playerInfo = playerinfo.load_players(playerCSV)
        print ('Loaded from file - ', playerCSV)

    elif strChoice == 'i':
        playerinfo.print_playerinfo(listTbl)
        continue
    
    else:
        print('General Error')
