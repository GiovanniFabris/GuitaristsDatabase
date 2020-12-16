"""
This module is the one that tests all the 4 functions
necessary to let the user interact with the database.

Each Test Case tests a Known valid and invalid entries.

tearDown and setUp functions were used as well
to set up mock variables and csv files needed
to test the functions.

"""

import unittest
from checker import Check
import adder as a
import csv_creator as d
import pandas as pd
import os


class TestName(unittest.TestCase):

    # this function will be run at the end of the
    # whole test process
    @classmethod
    def tearDownClass(cls):
        db = pd.DataFrame(pd.read_csv('players_bands.csv'))
        print(db)
        ind = db.loc[db["Players"] == "Daniel"].index.values
        db.drop(db.index[ind[0]], inplace=True)
        db.drop("Unnamed: 0", axis=1, inplace=True)
        db.to_csv("players_bands.csv")
        print(pd.DataFrame(pd.read_csv('example.csv')))
        os.remove("example.csv")

    # this one instead is run at the beginning
    # of each test
    def setUp(self):
        self.correct_g = "Jimmy Page"
        self.correct_b = "Led Zeppelin"
        self.new_g = "Daniel"
        self.dictionary = {"key": "value"}
        self.csv_name = "example.csv"

    def test_check_band(self):
        self.assertTrue(Check().check_band(self.correct_b))
        self.assertFalse(Check().check_band(self.correct_g))

    def test_check_guitarist(self):
        self.assertFalse(Check().check_guitarist(self.correct_b))
        self.assertTrue(Check().check_guitarist(self.correct_g))

    def test_adding_process(self):
        test1 = print("sorry, but " + self.correct_g +
                      " is already present in the database, thank you anyway")
        self.assertEqual(test1, a.add_element(self.correct_g))
        test2 = print("sorry, but " + self.correct_b +
                      " is already present in the database, thank you anyway")
        self.assertEqual(test2, a.add_element(self.correct_b))
        test3 = print("Thank you for your contribution!")
        self.assertEqual(test3, a.add_element(self.new_g, "g"))

    def test_database(self):
        self.assertEqual(d.database(self.dictionary, self.csv_name),
                         print("database created successfully "))


# by setting this up we can run this file
# on the command line without having
# having to call the unittest module.

if __name__ == "__main__":
    unittest.main()
