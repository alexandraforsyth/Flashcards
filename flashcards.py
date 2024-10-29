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


# JSON
# till text eval()
# pickle


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
#         
#     elif chosen_option == "2":
#         
    elif chosen_option == "3":
        create_flashdeck(input("\nNew flashdeck title  "))
#         
#     elif chosen_option == "4":
#         shutdown()
#     else:
#         while not chosen_option == "1" and not chosen_option == "2" and not chosen_option == "3" and not chosen_option == "4":
#             print("Please enter valid option.")
#             chosen_option = input("Option: ")
#         if chosen_option == "1":
#             
#         elif chosen_option == "2":
#             
#         elif chosen_option == "3":
#             
#         elif chosen_option == "4":
#             shutdown()  

def choose_practice_deck():
    deck_number = 0
    print("These are your flashdecks:")
    for deck in flashdecks:
        deck_number +=1
        print(f"{deck_number}) {deck[0]}")
    chosen_deck_input = int(input(f"Enter number of desired deck 1-{deck_number}: ")) -1
    chosen_deck = flashdecks[chosen_deck_input]
    practice(chosen_deck)
    
def practice(title):
    list_of_cards = load_file_as_list(title)
    for card in list_of_cards:
        if type(card) == dict: 
            print(card["question"])
            answer = input("Answer: ")
            if answer == card["answer"]:
                print("Correct")
            else:
                print("Incorrect")
# def flashdecks():
#     print

def create_flashdeck(title):
    new_flashdeck_file = open(title + ".txt", "a")
    create_flashcard(title)
    
def create_flashcard(title):
    file = open(title + ".txt", "a")
    question = "\"" + input("Enter question   ") + "\""
    answer = "\"" + input("Enter answer   ") + "\""
    
    file.write('{"question":'+ question + ', "answer":'+ answer + '}\n')
    file.close()
    view_flashdeck(title)
        
def load_file_as_list(title):
    with open(title + ".txt", 'r') as file:
        lines = file.readlines()
    list_of_dict = [json.loads(line.strip()) for line in lines]
    return(list_of_dict)


def view_flashdeck(title):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f"Flashdeck: {title}")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Questions:\n")
    count = 0
    for card in load_file_as_list(title):
        count +=1
        print(f"{count}) " + card["question"])
        
    print("\nWhat do you want to do?\n")
    print(f"a) Add new card \np) Practice \n1-{count}) Choose card to view")
    option = input("Choose option: ")
    if option == "a":
        create_flashcard(title)
    elif option == "p":
        practice(title)
    elif 1 <= int(option) <= count:
        view_card(title, int(option))
    
def view_card(title, card):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f"\nViewing card number {card} from deck {title}\n")
    list_of_cards = load_file_as_list(title)
    card = list_of_cards[card -1]
    print("Question: " + card["question"])
    print("Answer: " + card["answer"])
    

def shutdown():
    print("Flashdecks shutting down.")
    exit()
    
# main()

