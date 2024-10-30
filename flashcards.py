import json
import os

def splash():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("     Welcome to Flashdecks,\n a text-based flashcard program!")
    

def startup():
    splash()
    main()

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("1) Practice" + "\n" + "2) My Flashdecks" +"\n" + "3) New Flashdeck" + "\n" + "4) Exit")
    while True:
        chosen_option = input("\nOption: ")
        if chosen_option == "1":
            #Listar upp
            practice(list_choose_decks())
            break 
        elif chosen_option == "2":
            view_my_flashdecks()   
            break
        elif chosen_option == "3":
            create_flashdeck(input("\nNew flashdeck title  ")) 
            break
        elif chosen_option == "4":
            shutdown()
            break
        else:
            print("Please enter valid option.")
                

def load_file_as_list(title):
    #skapar en lista där varje element är en dictionare med frågor och svar
    with open(title + ".txt", 'r') as file:
        lines = file.readlines()
    list_of_dict = [json.loads(line.strip()) for line in lines]
    return(list_of_dict)

def flashdecks_names_list():
    #skapar en lista med namnen på filerna, men tar bort ändelsen .txt för att göra en snygg lista
    text_files_names = [file[:-4] for file in os.listdir(".") if file.endswith('.txt')]
    return(text_files_names)

def list_choose_decks():
    #en funktion som listar upp alla decks och låter användaren välja en
    deck_number = 0
    flashdecks = flashdecks_names_list()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("These are your flashdecks:")
    for deck in flashdecks:
        deck_number +=1
        print(f"{deck_number}) {deck}")
    print("\nChoose deck by entering its number or")
    print("b) Go back")
    while True: 
        chosen_deck_input = (input(f"\nChoose option: "))
        if str.isdigit(chosen_deck_input):
            chosen_deck_input = int(chosen_deck_input) -1
            chosen_deck_title = flashdecks[chosen_deck_input]
            break
        elif chosen_deck_input == "b":
            main()
            break
        else:
            print("Please enter valid option.")
        
    
    return(chosen_deck_title)  
    
def practice(title):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Practicing {title}!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    list_of_cards = load_file_as_list(title)
    correct = 0
    questions = 0
    for card in list_of_cards:
        if type(card) == dict:
            questions += 1
            print(card["question"])
            answer = input("Answer: ")
            if answer.lower() == card["answer"].lower():
                print("Correct")
                correct += 1
            else:
                print("Incorrect")
    print (f"You answered {correct} out of {questions} question(s) correctly. \n")
    main()

def create_flashdeck(title):
    open(title + ".txt", "a")
    create_flashcard(title)
    
def create_flashcard(title):
    file = open(title + ".txt", "a")
    question = "\"" + input("Enter question   ") + "\""
    answer = "\"" + input("Enter answer   ") + "\""
    
    file.write('{"question":'+ question + ', "answer":'+ answer + '}\n')
    file.close()
    view_flashdeck(title)

def view_my_flashdecks():
    #listar upp alla decks och den som väljs visas upp
    view_flashdeck(list_choose_decks())

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
    print(f"a) Add new card \np) Practice \n1-{count}) Choose card to view \n\nb) Go back")
    while True: 
        chosen_option = input("Choose option: ")
        if chosen_option == "a":
            create_flashcard(title)
            break
        elif chosen_option == "p":
            practice(title)
            break
        elif chosen_option == "b":
            view_my_flashdecks()
            break
        elif 1 <= int(chosen_option) <= count:
            view_card(title, int(chosen_option))
            break
        else:
            print("Please enter valid option.")

    
    
def view_card(title, card):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f"Viewing card number {card} from deck {title}\n")
    list_of_cards = load_file_as_list(title)
    card = list_of_cards[card -1]
    print("Question: " + card["question"])
    print("Answer: " + card["answer"])
    print("\nb) Go back")
    while True: 
        chosen_option = input("Choose option: ")
        if chosen_option == "b":
            view_flashdeck(title)
            break
        else:
            print("Please enter valid option.")

    
def shutdown():
    print("Flashdecks shutting down.")
    exit()
    
startup()
