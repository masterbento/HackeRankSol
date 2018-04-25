#!/bin/python3
import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    total = round(meal_cost+ (meal_cost*(tip_percent/100) + (meal_cost*(tax_percent/100))))
    #total = round(total)

    print("The total meal cost is "+str(total)+" dollars.")
