import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class AnalysisVisualiser:
    
    def __init__(self, all_text_stats):
        self.all_text_stats=all_text_stats
        
    #Below method displays the character frequency    
    def visualise_character_frequency(self):
        #below plots the data from all 6 data into horizontal bar graph as stacked
        plot=self.all_text_stats[['Edward_II_Marlowe','Hamlet_Shakespeare','Henry_VI_Part1_Shakespeare',
              'Henry_VI_Part2_Shakespeare','Jew_of_Malta_Marlowe','Richard_II_Shakespeare']].plot(kind='barh',stacked=True,
               title='Distribution of All letters',figsize=(18.5, 10.5))
        plot.set_xlabel('Relative frequency distribution') #naming the x-axis
        plot.set_ylabel('Letters') # naming the y-axis
        plt.savefig('Distribution of All letters.png') #saving the file as png
        plt.show()
        
    #Below method displays the punctuation frequency    
    def visualise_punctuation_frequency(self):
        #below plots the data from all 6 data into horizontal bar graph as stacked
        plot=self.all_text_stats[['Edward_II_Marlowe','Hamlet_Shakespeare','Henry_VI_Part1_Shakespeare',
              'Henry_VI_Part2_Shakespeare','Jew_of_Malta_Marlowe','Richard_II_Shakespeare']].plot(kind='barh',stacked=True,
               title='Distribution of Punctuation',figsize=(18.5, 10.5))
        plot.set_xlabel('Relative frequency distribution')#naming the x-axis
        plot.set_ylabel('Punctuation') # naming the y-axis
        plt.yticks(size=20)
        plt.savefig('Distribution of All Punctuation.png') #saving the file as png
        plt.show()

    #Below method displays the stopword frequency 
    def visualise_stopword_frequency(self):
        #below plots the data from all 6 data into horizontal bar graph as stacked
        plot=self.all_text_stats[['Edward_II_Marlowe','Hamlet_Shakespeare','Henry_VI_Part1_Shakespeare',
              'Henry_VI_Part2_Shakespeare','Jew_of_Malta_Marlowe','Richard_II_Shakespeare']].plot(kind='barh',stacked=True,
               title='Distribution of All Stop Words',figsize=(100,100))
        plot.set_ylabel('Stop_words') # naming the y-axis
        plt.yticks(size=20)
        plot.set_xlabel('Relative frequency distribution')#naming the x-axis
        plt.xticks(size=20)
        plt.savefig('Distribution of All Stop Words.png') #saving the file as png
        plt.show()
           
    #Below method displays the word length frequency     
    def visualise_word_length_frequency(self):
        #below plots the data from all 6 data into horizontal bar graph as stacked
        plot=self.all_text_stats[['Edward_II_Marlowe','Hamlet_Shakespeare','Henry_VI_Part1_Shakespeare',
              'Henry_VI_Part2_Shakespeare','Jew_of_Malta_Marlowe','Richard_II_Shakespeare']].plot(kind='barh',stacked=True,
               title='Distribution of different word length',figsize=(18.5, 10.5))
        plot.set_xlabel('Relative frequency distribution')#naming the x-axis
        plot.set_ylabel('Word_length') # naming the y-axis
        plt.savefig('Distribution of all word length.png') #saving the file as png
        plt.show()
        
    