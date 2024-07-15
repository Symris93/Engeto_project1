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
len_1 = 0
len_2 = 0
len_3 = 0
len_4 = 0
len_5 = 0
len_6 = 0
len_7 = 0
len_8 = 0
len_9 = 0
len_10 = 0
len_11 = 0
len_12 = 0
len_13 = 0




if username in registered.keys() and password == registered[username]:
    print(f"""----------------------------------------
Welcome to the app {username}
We have 3 texts to be analyzed.
----------------------------------------""")
    selection = int(input("Enter a number btw. 1 and 3 to select: "))
    if 0 < selection < 4:
        stripped = TEXTS[selection-1].replace(",","").replace(".","")
    else:
        print("Wrong number entered. Please try again and select between 1 and 3.")
        exit()
else:
    print("unregistered user, terminating the program..")
    exit()


words = stripped.split()

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

    if len(word) == 1:
        len_1 += 1
    elif len(word) == 2:
        len_2 += 1
    elif len(word) == 3:
        len_3 += 1
    elif len(word) == 4:
        len_4 += 1
    elif len(word) == 5:
        len_5 += 1
    elif len(word) == 6:
        len_6 += 1
    elif len(word) == 7:
        len_7 += 1
    elif len(word) == 8:
        len_8 += 1
    elif len(word) == 9:
        len_9 += 1
    elif len(word) == 10:
        len_10 += 1
    elif len(word) == 11:
        len_11 += 1
    elif len(word) == 12:
        len_12 += 1
    elif len(word) == 13:
        len_13 += 1

len_all = [
    (1, "*" * len_1),
    (2, "*" * len_2),
    (3, "*" * len_3),
    (4, "*" * len_4),
    (5, "*" * len_5),
    (6, "*" * len_6),
    (7, "*" * len_7),
    (8, "*" * len_8),
    (9, "*" * len_9),
    (10, "*" * len_10),
    (11, "*" * len_11),
    (12, "*" * len_12),
    (13, "*" * len_13)
]


print(f"""There are {word_count} words in the selected text.
There are {uppercase_word_count} titlecase words.
There are {all_uppercase_word_count} uppercase words.
There are {lowercase_word_count} lowercase words.
There are {numbers} numeric strings.
The sum of all the numbers {numbers_sum}
----------------------------------------
LEN|    OCCURENCES      |NR.
----------------------------------------""")
for len_ in len_all:
    print(f"{len_[0]:>3}|{len_[1]:<20}|{len(len_[1])}")