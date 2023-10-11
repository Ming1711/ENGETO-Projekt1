"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Kupeček
email: honzakupecek@gmail.com
discord: ming0092
"""

# Registrovaní uživatelé
USERS = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Předpřipravené texty
TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    '''
]

def authenticate_user():
    while True:
        username = input("username: ")
        password = input("password: ")
        if username in USERS and USERS[username] == password:
            print(f"Welcome to the app, {username}")
            return username
        else:
            print("unregistered user, terminating the program..")
            exit()

def analyze_text(text):
    words = text.split()
    word_lengths = []
    titlecase_words = 0
    uppercase_words = 0
    lowercase_words = 0
    numeric_strings = 0
    total_numeric = 0

    for word in words:
        # Počet slov
        word_lengths.append(len(word))
        
        # Počet slov začínajících velkým písmenem
        if word.istitle():
            titlecase_words += 1
        
        # Počet slov psaných velkými písmeny
        if word.isupper():
            uppercase_words += 1
        
        # Počet slov psaných malými písmeny
        if word.islower():
            lowercase_words += 1
        
        # Počet čísel (ne cifer) a suma čísel v textu
        if word.isdigit():
            numeric_strings += 1
            total_numeric += int(word)
        elif word.replace(",", "").isdigit():
            numeric_strings += 1
            total_numeric += int(word.replace(",", ""))

    print(f"There are {len(words)} words in the selected text.")
    print(f"There are {titlecase_words} titlecase words.")
    print(f"There are {uppercase_words} uppercase words.")
    print(f"There are {lowercase_words} lowercase words.")
    print(f"There are {numeric_strings} numeric strings.")
    print(f"The sum of all the numbers {total_numeric}")

    # Výpočet četností různých délek slov pro sloupcový graf
    word_length_counts = {i: word_lengths.count(i) for i in set(word_lengths)}
    sorted_word_length_counts = dict(sorted(word_length_counts.items()))

    print("----------------------------------------")
    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    for length, count in sorted_word_length_counts.items():
        print(f"{length:3}|{'*' * count: >13}|{count: >2}")

def main():
    username = authenticate_user()
    print("----------------------------------------")
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")

    while True:
        try:
            selection = int(input("Enter a number btw. 1 and 3 to select: "))
            if 1 <= selection <= 3:
                selected_text = TEXTS[selection - 1]
                analyze_text(selected_text)
                break
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()