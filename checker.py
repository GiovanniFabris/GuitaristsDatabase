"""
This module focuses on checking if the input
given by the user corresponds to one of the
instances present in the csv file
that contains the names of the guitarists and
bands.
"""
import pandas as pd


class Check:

    def check_guitarist(self, guitar_player):
        """
        This function controls if the input given
        by the user is present in the guitarists players
        column inside the guitarists csv file.
        """
        guitar_player = guitar_player.lower()
        db = pd.DataFrame(pd.read_csv('players_bands.csv'))
        players = db["Players"].str.lower()
        if guitar_player in players.values:
            return True
        return False

    def check_band(self, band_name):
        """
        This function controls if the input given
        by the user is present in the band
        column inside the guitarists csv file.
        """
        band_name = band_name.lower()
        db = pd.DataFrame(pd.read_csv('players_bands.csv'))
        bands = db["Bands"].str.lower()
        if band_name in bands.values:
            return True
        return False
