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

registered_users = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}
separator= "-" * 40

def prompt_for_input(prompt):
    """
    Prompts the user for input until a non-empty input is provided.

    Args:
    prompt (str): The prompt message to display to the user.

    Returns:
    str: The non-empty input provided by the user.
    """
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input
        print("Empty input. Try again...")

def authenticate_user(username, password, registered_users):
    """
    Authenticates the user against the registered users.
    """
    return password == registered_users.get(username)

def get_user_choice():
    """
    Prompts the user to enter a number between 1 and 3.
    Keeps prompting until a valid input is received.

    Returns:
    int: The validated user choice.
    """
    while True:
        choice = input("Enter a number btw. 1 and 3 to select: ")
        if choice.isnumeric():
            choice = int(choice)
            if 1 <= choice <= 3:
                return choice 
            else:
                print(f"{choice} is not between numbers 1-3. Please try again")
        else:
            print("Invalid input. Please enter a numeric value.")

def analyze_text(text):
    """
    Analyzes the text and prints statistics about word lengths, case, and numbers.
    """
    words = [word.strip(',.?!') for word in text.split()]
    word_lengths = [len(word) for word in words]
    title_case = [word for word in words if word.istitle()]
    upper_case = [word for word in words if word.isupper() and word.isalpha()]
    lower_case = [word for word in words if word.islower()]
    numeric = [int(word) for word in words if word.isdigit()]

    print(f"{separator}\nThere are {len(words)} words in the selected text.")
    print(f"There are {len(title_case)} titlecase words.")
    print(f"There are {len(upper_case)} uppercase words.")
    print(f"There are {len(lower_case)} lowercase words.")
    print(f"There are {len(numeric)} numeric strings.")
    print(f"The sum of all the numbers is {sum(numeric)}.\n{separator}")
    print(f"LEN|  OCCURENCES  |NR.\n{separator}")

    word_length_counts = {}
    for lenght in word_lengths:
        word_length_counts[lenght] = word_length_counts.get(lenght, 0) + 1

    for lenght in sorted(word_length_counts):
        count = word_length_counts[lenght]
        print(f"{lenght:3}|{'*' * count:14}|{count}")

def main():
    """
    Main function to run the text analysis program.
    """
    username = prompt_for_input("Enter your username: ")
    password = prompt_for_input("Enter your password: ")
    if authenticate_user(username, password, registered_users):
        print(f"{separator}\nWelcome to the app, {username.title()}")
    else:
        print("Unregistered user, terminating the program...")
        exit()
    print(f"We have {len(TEXTS)} texts to be analyzed.\n{separator}")
    choice = get_user_choice()
    choosen_text = TEXTS[choice - 1]
    analyze_text(choosen_text)

if __name__ == "__main__":
    main()
