"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Fúzik
email: fuzik@atlas.cz
discord: symris93
"""

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

registered = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }


username = input("username:")
password = input("password:")

word_count = 0
uppercase_word_count = 0
all_uppercase_word_count = 0
lowercase_word_count = 0
numbers = 0
numbers_sum = 0





if username in registered.keys() and password == registered[username]:
    print(f"""----------------------------------------
Welcome to the app {username}
We have 3 texts to be analyzed.
----------------------------------------""")
    selection = input("Enter a number btw. 1 and 3 to select: ")
    if selection.isnumeric() and 0 < int(selection) < 4:
        stripped = TEXTS[int(selection)-1].replace(",","").replace(".","")    
    else:
        print("Wrong input. Please try again and type \"1\", \"2\" or \"3\".")
        exit()
else:
    print("unregistered user, terminating the program..")
    exit()


words = stripped.split()
word_length_counts = {}

for word in words:
    word_count += 1

    if word[0].isupper():
        uppercase_word_count += 1

    if word.isupper() and word.isalpha():
        all_uppercase_word_count += 1

    if word.islower():
        lowercase_word_count += 1
    
    if word.isnumeric():
        numbers += 1
        numbers_sum += int(word)

    length = len(word)
    if length in word_length_counts:
        word_length_counts[length] += 1
    else:
        word_length_counts[length] = 1


print(f"""There are {word_count} words in the selected text.
There are {uppercase_word_count} titlecase words.
There are {all_uppercase_word_count} uppercase words.
There are {lowercase_word_count} lowercase words.
There are {numbers} numeric strings.
The sum of all the numbers {numbers_sum}
----------------------------------------
LEN|    OCCURENCES      |NR.
----------------------------------------""")
for length, count in sorted(word_length_counts.items()):
    print(f"{length:>3}|{(count*"*"):<20}|{count}")
