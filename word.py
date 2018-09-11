import pandas as pd
from bs4 import BeautifulSoup #used in extracting stop words from website
import urllib.request #used in extracting stop words from website

class WordAnalyser:
    def __init__(self):
        #intialising all required data frames
        self.word_df=pd.DataFrame()
        self.stopword_df=pd.DataFrame()
        self.word_len=pd.DataFrame()
    
    def __str__(self):
        print("The word frequencey:\n",self.word_df)
        return " "
    
    #Below method tokenises only words and store the output in a data frame
    def analyse_words(self, tokenised_list):
        self.tokenised_list=tokenised_list
        wordfreq=[self.tokenised_list.count(w) for w in self.tokenised_list] #counts the frequency of words in a data frame
        self.word_df=pd.DataFrame([self.tokenised_list,wordfreq]).transpose()
        self.word_df.columns=['word','count'] #renames the column
        self.word_df=self.word_df.drop_duplicates() #drops duplicates
        self.word_df=self.word_df.reset_index(drop=True) #resets the index
        self.word_df.index=self.word_df.index+1 #reset teh index to start from 1
    
    #Below metod reads the websites and retrieves the stop words from website and stores in a list
    def get_stopword(self):
        address = 'http://www.lextek.com/manuals/onix/stopwords1.html'
        response = urllib.request.urlopen(address)
        html = response.read()
        soup = BeautifulSoup(html,"lxml")
        table = soup.find("pre").contents[0]
        self.stopwd_list=list(table[121:].split())
        return self.stopwd_list
    
    #Below method extracts stopsword frequency from a given data frame
    def get_stopword_frequency(self):
        self.stop_word_list=self.get_stopword() #extract the stop word list from website
        
        #extract only stop words from the tokenised list ( which is also sent to analyse_words() )
        stop_words_fromlist=[word for word in self.tokenised_list if word in self.stop_word_list]
        
        stopword_freq=[stop_words_fromlist.count(w) for w in stop_words_fromlist]
        self.stopword_df=pd.DataFrame([stop_words_fromlist,stopword_freq]).transpose()
        self.stopword_df.columns=['stop_word','count']
        self.stopword_df=self.stopword_df.drop_duplicates()
        self.stopword_df=self.stopword_df.reset_index(drop=True)
        self.stopword_df.index=self.stopword_df.index+1
        return self.stopword_df
        
    #Below method is used to retrieve the word length frequency from a given tokenised list    
    def get_word_length_frequency(self):
        word_df=pd.DataFrame(self.tokenised_list) #extract the data from 'analyse word'
        word_df['wordlen']=word_df[0].apply(lambda x: len(x)) #add a new column with name wordlen which has count of length of words
        word_df.columns=['word','wordlen'] # selecting required columns to display
        self.word_len=word_df.groupby('wordlen',as_index=False).count() # using group by arrange the data
        self.word_len.columns=['wordlen','count'] #selecting required data frame
        self.word_len.index=self.word_len.index+1
        return self.word_len
        