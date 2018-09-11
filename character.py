import pandas as pd
import numpy as np
import re
import string

class CharacterAnalyser:
    
    def __init__(self):
        #all required data frames are defined
        self.char_df=pd.DataFrame()
        self.pun_df=pd.DataFrame()
        self.letter_df=pd.DataFrame()
        
        
    def __str__(self):
        print(self.char_df)
        return " "

    #Below method tokenised the individual characters, and stores in a data frame
    def analyse_characters(self, tokenised_list):
        self.list=tokenised_list
        charfreq = [self.list.count(w) for w in self.list] # a list comprehension to count the freqeuency of the characters
        self.char_df = pd.DataFrame([self.list, charfreq]).transpose()
        self.char_df.columns =['char','count'] # renaming the columns
        self.char_df=self.char_df.drop_duplicates() # removing all the duplicates
        self.char_df=self.char_df.reset_index(drop=True) #resetting the index
        self.char_df.index=self.char_df.index+1 #intialsing the index to start from 1
        
    #Below method counts the frequencey of the punctuations and returns it    
    def get_punctuation_frequency(self):
        self.pun_df=self.char_df.loc[self.char_df['char'].isin(['.' , '?', ',' , ';', ':', '!', '&' , "'"])]
        self.pun_df=self.pun_df.reset_index(drop=True)
        self.pun_df.index=self.pun_df.index+1
        return self.pun_df
    
    #Below method counts the frequencey of the letters and returns it  
    def get_letter_frequency(self):
        self.letter_df=self.char_df.loc[self.char_df['char'].isin(list(string.ascii_lowercase))]
        self.letter_df=self.letter_df.reset_index(drop=True)
        self.letter_df.index=self.letter_df.index+1
        return self.letter_df
