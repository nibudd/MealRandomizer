# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:46:28 2019

@author: nibudd
"""

import os
from random import seed, sample

def mealRandomizer(n=3):
    """
    Prints a list of n meals from MealList.txt.
    """
    fname = os.getcwd() + "\MealList.txt"
    with open(fname, "r") as f:
        meals = f.read().splitlines()
        
    seed()
    return sample(meals, n)
    
    
if __name__ == "__main__":
    print(mealRandomizer())