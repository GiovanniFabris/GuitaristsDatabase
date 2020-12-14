"""
This module focuses on checking if the input
given by the user corresponds to one of the 
instances present in the csv file
that contains the names of the guitarists and 
bands.
"""

import csv
import pandas as pd


class Check:


    def check_guitarist(self, guitar_player):
        """
        This function controls if the input given 
        by the user is present in the guitarists players
        column inside the guitarists csv file.
        """
        db = pd.DataFrame(pd.read_csv('players_bands.csv'))
        if guitar_player in db["Players"].values:
            return True
        return False
                   
                                  
    def check_band(self, band_name):
        """
        This function controls if the input given 
        by the user is present in the band
        column inside the guitarists csv file.
        """
        db = pd.DataFrame(pd.read_csv('players_bands.csv'))
        if band_name in db["bands"].values:
            return True
        return False