__author__="David Marienburg"
__version__="1.0"
__LastUpdate__="4/8/2019"


import pandas as pd
import numpy as np

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class FindPotentialGPDPT:
    """
    Initialize the class and the four raw dataframes containing participants
    entered into shelter, served by the resouce center, entered into case
    management, and those participants contact information.

    Each of these sheets should be added to a separate dataframe that will
    then be sliced and checked for consistency prior to being returned as an
    Excel spreadsheet.
    """
    def __init__(self):
        file = askopenfilename(
            title="Open the Non-GPD Vets In Shelter and Resource Center report"
        )
        self.shelter = pd.read_excel(file, sheet_name="ShelterEntryData")
        self.day = pd.read_excel(file, sheet_name="ResourceCenterData")
        self.cm = pd.read_excel(file, sheet_name="CMProviderEntryData")
        self.contact = pd.read_excel(file, sheet_name="PTContactData")

    def save(self, final_df):
        """
        Save an Excel spreadsheet containing participants who are vets and are
        either accessing services at the resource center or staying at a
        shelter but are not being served by case management.
        """
        pass

    def filter_and_concat(self):
        """
        Filter the self.day and self.shelter dataframes so that they do not
        contain participants who are currently being served with casemanagement
        services then concatenate the two dataframes into a single data frame
        which will then be returned.
        """
        pass

    def add_contact_info(self, all_possible_vets=self.filter_and_concat()):
        """
        Perform a left merge between the all_possible_vets dataframe (which is
        the output of the filter_and_concat method) and the self.contact
        dataframe, then return the resulting dataframe.
        """
        pass
