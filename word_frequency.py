#Jason Aylward
#January 14, 2015
#Homework 3

import sys

def format_text(original_text):
    """Receives a string and returns a list of acceptable words"""
    new_text = original_text.lower()
    bad_chars = ["\n","\r","\t",".",",",'"',"?","!","]","[",
                "0","1","2","3","4","5","6","7","8","9","'",
                "(",")","@","#","$","%","^","&","*","_","+",
                ":",";","/","http","www","`","~"]
    new_text = new_text.replace("--", " ")
    for bad_char in bad_chars:
         new_text = new_text.replace(bad_char,' ')
    text = new_text.split(' ')
    clean_text = []
    for word in text:
        #Remove empty words and remaining s's from contractions and possessives
        if(word != "" and word != "s"):
            clean_text.insert(len(clean_text),word)
    return clean_text

def word_frequency(input_text):
    """Receives a string
    and returns a dictionary of words and their counts
    also prints a histogramic list of the top 20 words"""
    word_list = format_text(input_text)
    dict_of_words = {}
    for word in word_list:
        try:
            dict_of_words[word] += 1
        except:
            dict_of_words[word] = 1
    analyze_dict(dict_of_words)
    return dict_of_words

def analyze_dict(dict_of_counts):
    """Receives a dictionary of words and their word counts
    sorts the dictionary and prints the top 20 occurring words"""
    word_list = sorted(dict_of_counts.items(), key=lambda x: x[1], reverse = True)
    for x in range(0,20):
        try:
            #Cleaning up the histogram basing spaces on word-length
            if len(word_list[x][0]) <= 3:
                print("{}. {}: {} times   \t\t{}".format(x+1,word_list[x][0],word_list[x][1],histogram(word_list[x][1],word_list[0][1])))
            else:
                print("{}. {}: {} times\t\t{}".format(x+1,word_list[x][0],word_list[x][1],histogram(word_list[x][1],word_list[0][1])))
        except:
            print("Sorry. There are less than twenty words.")
            break
    print("\n")

def histogram(current,max_count):
    """Returns string of #'s of an appropriate length"""
    normalizer = 50/max_count
    hash_string = " "
    count = 0
    while count < (current*normalizer):
        hash_string = hash_string + "#"
        count += 1
    return hash_string


"""                     Start of program                    """
try:
    with open((sys.argv[1])) as input_file:
        input_lines = input_file.readlines()
except:
    with open("sample.txt") as input_file:
        input_lines = input_file.readlines()

#join all the lines of text by " "
input_string = " ".join(input_lines)
dict_of_words = word_frequency(input_string)
