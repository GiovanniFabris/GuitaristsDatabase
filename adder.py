"""
The adder module has a single
function with the purpose 
of appending inside the dataset
the names of the bands/guitarists
he/she inputs.

The input will be checked to 
see if it is already inside the 
database.

The user will be able to choose 
whether the name he put as input 
is of a guitarist or band, and then
input later on the second name.

It is necessary for the user to 
input a string that is not empty.

"""

import csv
import pandas as pd
from checker import Check


def add_element(g_or_b, response=""):

    """
    This function comes into play once the user inputs a value
    that is not to be found inside the database, or when, after 
    the input, the user writes the optional argument -a.
    It asks if the input is a name of a band or a guitarist, 
    then it asks for the missing name, and proceeds to add both 
    values under the right columns in our database.
    """
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
