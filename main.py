from collections import Counter
import time

TEXTS = ['''  
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {"Bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

c = ("-" * 50)

# log

def login():

    username = input("username: ")
    password = input("password: ")

    if username in users:
        if users[username] == password:
            print(c, "\nWelcome to the app,", username, "\nWe have 3 texts to be analyzed.")
        else:
            print("Incorrect password, terminating the program..")
            exit()
    else:
        print("Unregistered user, terminating the program..")
        exit()

# usr_def_text

def textselect():

    txtsel = input("Enter a number btw. 1 and 3 to select:")
    
    if not txtsel.isnumeric():
        print("Bad input, terminating the program..")
        exit()
    
    txtsel = int(txtsel)
    if txtsel > 3 or txtsel < 1:
        print("Bad number, terminating the program..")
        exit()
    
    Texsts = TEXTS[txtsel - 1]
    print(c)
    print("Text number:", txtsel)
    print(Texsts)
    print(c)
    return Texsts

# an_text

def analyze_text(Texsts):
    
    words = Texsts.split()
    num_words = len(words)
    num_capitalized = sum(1 for word in words if word[0].isupper())
    num_all_caps = sum(1 for word in words if word.isupper())
    num_lowercase = sum(1 for word in words if word.islower())
    num_int = sum(1 for word in words if word.isdigit())
    num_sum = sum(int(word) for word in words if word.isdigit())

    print(f"There are {num_words} words in the selected text.")
    print(f"There are {num_capitalized} titlecase words")
    print(f"There are {num_all_caps} uppercase words.")
    print(f"There are {num_lowercase} lowercase words")
    print(f"There are {num_int} numeric strings")
    print(f"The sum of all the numbers is {num_sum}")
    print(c)

# graf_text

def word_graf(Texsts):

    print("LEN| OCCURRENCES", " " * 8,"|NR.")
    words = Texsts.split()
    len_word = [len(word) for word in words]
    len_num = Counter(len_word)
    max_length = max(len_num)
    
    for length in range(min(len_word), max_length + 1):
        if length in len_num:
            print(f"{length:>2} | {'*' * len_num[length]:<20} | {len_num[length]}")

# main

def main():

    print(c,"Text Analyzer",c,sep="\n")
    login() 
    print(c)
    Texsts = textselect()

    for _ in range(3):
        print(f"Analyzing text..")
        time.sleep(1)
    
    print(c,"Text analyzed!",c,sep="\n")
    analyze_text(Texsts)
    word_graf(Texsts)
    print(c)

main()
