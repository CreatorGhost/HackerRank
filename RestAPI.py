#!/bin/python3

import math
import os
import random
import re
import sys



import requests 
#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalGoals(team, year):
    c=0
    r=requests.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1='+str(team)+'&page=1').json()
    total1=r['total_pages']
    per2=r['per_page']
    for j in range(1,total1+1):
         r=requests.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1='+str(team)+'&page='+str(j)).json()
         try:
            for i in range(0,per2):
                team1=r['data'][i]['team1goals']
                c+=int(team1)
         except:
            pass

        
    r1=requests.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team2='+str(team)+'&page=1').json()
    total2=r1['total_pages']
    per2=r['per_page']
    for j in range(1,total2+1):
         r1=requests.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team2='+str(team)+'&page='+str(j)).json()
         try:
            for i in range(0,per2):
                team2=r1['data'][i]['team2goals']
                c+=int(team2)
         except:
            pass
    return c
'''
PASTE   ABOVE THE if __name__ == '__main__':
'''
