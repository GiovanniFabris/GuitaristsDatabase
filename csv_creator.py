"""
this module contains a function
that focuses on creating
a csv file from the dictionary given at
the beginning of the project
"""
import csv
from list_of_guitarists import list_of_guitarists
import pandas as pd


def database(dictionary, name_csv="players_bands.csv"):
    """
    the following function takes the elements present
    in the dictionary and places them into a csv file
    named guitarists.csv that we will use as our database.
    We will be able to add new bands and guitarists then.
    """

    g_b = []
    for key, value in dictionary.items():
        g_b.append([key, value])
    df = pd.DataFrame(g_b, columns=["Players", "Bands"])
    df.to_csv(name_csv)
    return print("database created successfully ")


database(list_of_guitarists)
