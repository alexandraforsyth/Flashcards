import json
math_flashdeck = [
    "Matte 3",
    {"question":"5+2?", "answer":"7", "hint":"6+1"},
    {"question":"5+3?", "answer":"8", "hint":"7+1"},
    ]

it_flashdeck = [
    "IT 3",
    {"question":"Hur många bit är en byte?", "answer":"8", "hint":"1000"},
    ]

flashdecks = [
    math_flashdeck,
    it_flashdeck,
    ]

def splash():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("     Welcome to Flashdecks,\n a text-based flashcard program!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def main():
    splash()
    print("1) Practice" + "\n" + "2) My Flashdecks" +"\n" + "3) New Flashdeck" + "\n" + "4) Exit")
    chosen_option = input("\nOption: ")
    if chosen_option == "1":
        choose_practice_deck()
    elif chosen_option == "2":
        deck_number = 0
        print("These are your flashdecks:")
        for deck in flashdecks:
            deck_number +=1
            print(f"{deck_number}) {deck[0]}")       
    elif chosen_option == "3":
        create_flashdeck(input("\nNew flashdeck title  "))  
    elif chosen_option == "4":
        shutdown()
    else:
        while not chosen_option == "1" and not chosen_option == "2" and not chosen_option == "3" and not chosen_option == "4":
            print("Please enter valid option.")
            print("1) Practice" + "\n" + "2) My Flashdecks" +"\n" + "3) New Flashdeck" + "\n" + "4) Exit")
            chosen_option = input("Option: ")
        if chosen_option == "1":
            choose_practice_deck()  
        elif chosen_option == "2":
            deck_number = 0
            print("These are your flashdecks:")
            for deck in flashdecks:
                deck_number +=1
                print(f"{deck_number}) {deck[0]}")    
        elif chosen_option == "3":
            create_flashdeck(input("\nNew flashdeck title  "))
        elif chosen_option == "4":
            shutdown()  

def choose_practice_deck():
    deck_number = 0
    print("These are your flashdecks:")
    for deck in flashdecks:
        deck_number +=1
        print(f"{deck_number}) {deck[0]}")
    chosen_deck_input = int(input(f"Enter number of desired deck 1-{deck_number}: ")) -1
    chosen_deck = flashdecks[chosen_deck_input]
    practice(chosen_deck)
    
def practice(flashdeck):
    correct = 0
    for card in flashdeck:
        if type(card) == dict: 
            print(card["question"])
            answer = input("Answer: ")
            if answer == card["answer"]:
                print("Correct")
                correct += 1
            else:
                print("Incorrect")
    print (f"You got {correct} out of {len(flashdeck)-1} question(s) correctly.")
    
def create_flashdeck(title):
    new_flashdeck_file = open(title + ".txt", "a")
    create_flashcard(title)
    
def create_flashcard(title):
    file = open(title + ".txt", "a")
    question = "\"" + input("Enter question   ") + "\""
    answer = "\"" + input("Enter answer   ") + "\""
    
    file.write('{"question":'+ question + ', "answer":'+ answer + '}\n')
    file.close()
    add_another = input("Do you want to add another one? (y/n) ")
    if add_another == "y":
        create_flashcard(title)
    else:
        main()
        
def load_file_as_list(title):
    with open(title + ".txt", 'r') as file:
        lines = file.readlines()
    list_of_dict = [json.loads(line.strip()) for line in lines]
    return(list_of_dict)


def view_flashdeck(title):
    print(f"FLashdeck: {title}")
    for card in load_file_as_list(title):
        print(card["question"])
        

def shutdown():
    print("Flashdecks shutting down.")
    exit()
    
# main()
