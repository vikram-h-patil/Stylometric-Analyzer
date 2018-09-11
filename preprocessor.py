import re
class Preprocessor:
    
    def __init__(self):
        self.token_word_list=[] # list to store the tokensied word
        self.token_punc_list=[] # list to store the tokensied punctuation
        self.token_punc_char_list=[] # list to store the tokensied character 
        
        
    def __str__(self):
        print("The individual words are:\n")
        print(self.token_word_list)
        print("---------------------------------")
        print("\nThe individual punctuations are:\n")
        print(self.token_punc_list)
        print("---------------------------------")
        print("\n the individual letters and char are:\n")
        print(self.token_punc_char_list)
        return " "
        
        
        
    def tokenise_word(self, input_sequence):
        self.input_sequence=input_sequence
        pat_word = r"[\w]+"
        self.token_word_list=re.findall(pat_word,input_sequence.lower()) # this step extracts all the words from the list
        pat_punc=r"[.?,;:!&']"
        self.token_punc_list=re.findall(pat_punc,input_sequence.lower()) # this step extract all the punctuation from the list
        pat_punc2=r"[.?,;:!&'\w]"
        self.token_punc_char_list=re.findall(pat_punc2,input_sequence.lower())
        # this step extracts all the characters, including the punctutation
        
 
    def get_tokenised_word_list(self):
        return self.token_word_list
 
    def get_tokenised_punc_list(self):
        return self.token_punc_list
    
    def get_tokenised_punc_char_list(self):
        return self.token_punc_char_list
    