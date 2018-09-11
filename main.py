import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from preprocessor import Preprocessor #importing task1 file
from character import CharacterAnalyser #importing task2 file
from word import WordAnalyser #importing task3 file
from visualiser import AnalysisVisualiser # importing task4 file
import sys


#Making the objects of the respective classes
p=Preprocessor()
c=CharacterAnalyser()
w=WordAnalyser()



#function to convert normal df into relative df
def rel_func(accept_df):
    accept_df=accept_df
    total=sum(accept_df['count']) #counts the total of the column with counts
    accept_df['rel_freq']=  (accept_df['count']/total) #calculate the reklative frequency
    return accept_df

#Below method performs required processing of data and return the relative frequency df
def perform_processing(input_file):
    input_file=input_file
    p.tokenise_word(input_file) #send the words to get tokenised
    tokenised_punc_char_list=p.get_tokenised_punc_char_list() # retrieves the tokenised list which contains punctuation and characters
    c.analyse_characters(tokenised_punc_char_list) #retrieves the punctuation frequency

    #Required for task 4
    pun_freq=c.get_punctuation_frequency() #store the punctuation frequency
    letter_freq=c.get_letter_frequency()  #store the letter frequency
    
    analyse_words=p.get_tokenised_word_list() #get the tokensied word list
    w.analyse_words(analyse_words) #send it for processing
    #Required for task 4
    stopword_freq=w.get_stopword_frequency() #store the stopword frequency
    word_length_freq=w.get_word_length_frequency() #store the word length frequency

    #relative freq of pun
    pun_rel_freq=rel_func(pun_freq) #convert normal df into relative frequency df
    pun_rel_freq.set_index('char', inplace=True)
    pun_rel_freq=pun_freq[['rel_freq']]
   
    #relative freq of letter
    letter_rel_freq=rel_func(letter_freq) #convert normal df into relative frequency df
    letter_rel_freq.set_index('char', inplace=True)
    letter_rel_freq=letter_rel_freq[['rel_freq']]

    #relative freq of stop word
    stopword_rel_freq=rel_func(stopword_freq) #convert normal df into relative frequency df
    stopword_rel_freq.set_index('stop_word', inplace=True)
    stopword_rel_freq=stopword_rel_freq[['rel_freq']]

    #relative freq of stop word length
    wordlen_rel_freq=rel_func(word_length_freq) #convert normal df into relative frequency df
    wordlen_rel_freq.set_index('wordlen', inplace=True)
    wordlen_rel_freq=wordlen_rel_freq[['rel_freq']]
    
    return pun_rel_freq,letter_rel_freq,stopword_rel_freq,wordlen_rel_freq

#Below method is used to implement the visualisation
def visualise(selection,accept_stats_df):
    if selection == 'pun':  # if the visualisation is punctuation then proceed
        a=AnalysisVisualiser(accept_stats_df)
        a.visualise_punctuation_frequency()
        
    elif selection == 'letter': # if the visualisation is letter then proceed
        a=AnalysisVisualiser(accept_stats_df)
        a.visualise_character_frequency()
        
    elif selection == 'stopword': # if the visualisation is stop word then proceed
        a=AnalysisVisualiser(accept_stats_df)
        a.visualise_stopword_frequency()
        
    else: # else the visualisation is word length and proceed
        a=AnalysisVisualiser(accept_stats_df)
        a.visualise_word_length_frequency()
    

def main():
    try:
        #Read the 6 files and store them
        with open('Edward_II_Marlowe.tok', 'r') as input_file:
            edward_inputfile = input_file.read()
        input_file.close()

        with open('Hamlet_Shakespeare.tok', 'r') as input_file:
            hamplet_inputfile = input_file.read()
        input_file.close()

        with open('Henry_VI_Part1_Shakespeare.tok', 'r') as input_file:
            henry_part1_inputfile = input_file.read()
        input_file.close()

        with open('Henry_VI_Part2_Shakespeare.tok', 'r') as input_file:
            henry_part2_inputfile = input_file.read()
        input_file.close()

        with open('Jew_of_Malta_Marlowe.tok', 'r') as input_file:
            jew_inputfile = input_file.read()
        input_file.close()

        with open('Richard_II_Shakespeare.tok', 'r') as input_file:
            richard_inputfile = input_file.read()
        input_file.close()

        #in below step send the individual input file to processing and the return has respective frequency of statistics
        edward_pun,edward_letter,edward_stopword,edward_wordlen=perform_processing(edward_inputfile) 
        hamlet_pun,hamlet_letter,hamlet_stopword,hamlet_wordlen=perform_processing(hamplet_inputfile)
        henry_part1_pun,henry_part1_letter,henry_part1_stopword,henry_part1_wordlen=perform_processing(henry_part1_inputfile)
        henry_part2_pun,henry_part2_letter,henry_part2_stopword,henry_part2_wordlen=perform_processing(henry_part2_inputfile)
        jew_pun,jew_letter,jew_stopword,jew_wordlen=perform_processing(jew_inputfile)
        richard_pun,richard_letter,richard_stopword,richard_wordlen=perform_processing(richard_inputfile)

        # Merge total Letter from 6 files into single df and print
        total_letter_df=pd.DataFrame()
        total_letter_df=pd.concat([edward_letter,hamlet_letter,henry_part1_letter,henry_part2_letter,jew_letter,richard_letter],axis=1)
        total_letter_df=total_letter_df.fillna(0) #converting all nan into 0
        total_letter_df.columns=['Edward_II_Marlowe','Hamlet_Shakespeare','Henry_VI_Part1_Shakespeare',
                              'Henry_VI_Part2_Shakespeare','Jew_of_Malta_Marlowe','Richard_II_Shakespeare']
        print("\n                       ---------Comparison of all letter types---------\n",total_letter_df)




        # Merge total punctuation from 6 files into single df and print
        total_pun_df=pd.DataFrame()
        total_pun_df=pd.concat([edward_pun,hamlet_pun,henry_part1_pun,henry_part2_pun,jew_pun,richard_pun],axis=1)
        total_pun_df=total_pun_df.fillna(0) #converting all nan into 0
        total_pun_df.columns=['Edward_II_Marlowe','Hamlet_Shakespeare','Henry_VI_Part1_Shakespeare',
                              'Henry_VI_Part2_Shakespeare','Jew_of_Malta_Marlowe','Richard_II_Shakespeare']
        print("\n\n                       ---------Comparison of all puncutation types---------\n",total_pun_df)



        # Merge total stop word from 6 files into single df and print
        total_stopword_df=pd.DataFrame()
        total_stopword_df=pd.concat([edward_stopword,hamlet_stopword,henry_part1_stopword,henry_part2_stopword
                                     ,jew_stopword,richard_stopword],axis=1)
        total_stopword_df=total_stopword_df.fillna(0) #converting all nan into 0
        total_stopword_df.columns=['Edward_II_Marlowe','Hamlet_Shakespeare','Henry_VI_Part1_Shakespeare',
                              'Henry_VI_Part2_Shakespeare','Jew_of_Malta_Marlowe','Richard_II_Shakespeare']
        print("\n\n                       ---------Comparison of all stopwords---------\n",total_stopword_df)



        # Merge total word length from 6 files into single df and print
        total_wordlen_df=pd.DataFrame()
        total_wordlen_df=pd.concat([edward_wordlen,hamlet_wordlen,henry_part1_wordlen,henry_part2_wordlen,jew_wordlen,
                                    richard_wordlen],axis=1)
        total_wordlen_df=total_wordlen_df.fillna(0) #converting all nan into 0
        total_wordlen_df.columns=['Edward_II_Marlowe','Hamlet_Shakespeare','Henry_VI_Part1_Shakespeare',
                              'Henry_VI_Part2_Shakespeare','Jew_of_Malta_Marlowe','Richard_II_Shakespeare']
        print("\n\n                       ---------Comparison of different word lengths---------\n",total_wordlen_df)

        
        #Next step perform the visualisation of individual relative frequencies
        visualise('pun',total_pun_df)
        visualise('letter',total_letter_df)
        visualise('stopword',total_stopword_df)
        visualise('wordlength',total_wordlen_df)

        #Next step prints the output of all 4 statistics into output file
        output_simple=open('output_statistics.txt','w')
        sys.stdout = output_simple
        print("\n       ---------Comparison of all letter types---------\n",total_letter_df)
        print("\n\n     ---------Comparison of all puncutation types---------\n",total_pun_df)
        print("\n\n     ---------Comparison of all stopwords---------\n",total_stopword_df)
        print("\n\n     ---------Comparison of different word lengths---------\n",total_wordlen_df)
        output_simple.close()
        
    except IOError:
        print("Cannot open file",input_file)
    except RuntimeError:
        print("A run-time error has occured")

    
if __name__ == "__main__":
    main()
