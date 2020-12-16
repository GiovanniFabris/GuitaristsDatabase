"""
In this module there is 
a function that lets the user
input a name of a guitarist or 
a band and then add it to the database
if it is not already part of it.

The system will require the user to put
any string input, but he/she is not allowed to 
put an empty string.

The function also has a default parameter useful
in the testing process of the adder.
"""
import csv
import pandas as pd
from checker import Check


def add_element(g_or_b, response=""):
    db = pd.DataFrame(pd.read_csv('players_bands.csv'))
    if Check().check_band(g_or_b):
        return print("sorry, but " + g_or_b + " is already present in the database, thank you anyway")
    elif Check().check_guitarist(g_or_b):
        return print("sorry, but " + g_or_b + " is already present in the database, thank you anyway")
    else:
        if response == "g":
            name1 = "g"
            name2 = "Daniel's Band"
        elif response == "b":
            name1 = "b"
            name2 = "Daniel"
        else:
            name1 = input("Is he a guitarist or is it a band (g or b) -> ")
        if name1 == "b":
            if response == "":
                name2 = input("Now enter the name of the guitarist -> ")
                while(name2 == ""):
                    name2 = input("You can't enter nothing... so please... put anything -> ")
            with open('players_bands.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                row = len(db)
                newFileWriter.writerow([row, name2, g_or_b])
            return print("Thank you for your contribution!")
        elif name1 == "g":
            if response == "":
                name2 = input("Now enter the name of the band -> ")
                while(name2 == ""):
                    name2 = input("You can't enter nothing... so please... put anything -> ")
            with open('players_bands.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                row = len(db)
                newFileWriter.writerow([row, g_or_b, name2])
            return print("Thank you for your contribution!")
        else:
            return print("you need to input either g or b")
