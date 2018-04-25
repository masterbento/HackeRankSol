#!/bin/python3

<<<<<<< HEAD
import sys
=======
import sys,math
>>>>>>> a0faba13070f69c03cb4eadb313a1d6bbc841448

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

<<<<<<< HEAD
    total = round(meal_cost+ (meal_cost*(tip_percent/100) + (meal_cost*(tax_percent/100))))
    #total = round(total)
=======


    total = meal_cost+ (meal_cost*(tip_percent/100) + (meal_cost*(tax_percent/100)))
    total = round(total)
>>>>>>> a0faba13070f69c03cb4eadb313a1d6bbc841448
    print("The total meal cost is "+str(total)+" dollars.")
