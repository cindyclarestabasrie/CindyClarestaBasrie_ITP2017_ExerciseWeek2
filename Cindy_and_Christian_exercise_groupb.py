your_name = str(input("Tell us your name: "))
endings = ["Teehee, program stopped.", "Oh, it closed.", "Nooooooo", "Don't cry, you can keep trying."]

choice_cr = ["crash", "Crash"]
choice_wrong = ["Wrong code", "wrong code"]
choice_close = ["Close", "close"]
choice_close2 = ["Close it", "close it"]
choice_cont = ["Continue", "continue"]
choice_err = ["Error", "error"]
choice_prob = ["Problems with app", "problems with app"]
choice_try = ["Try again", "try again"]
choice_new = ["New code", "new code"]
choice_no = ["No", "no"]
choice_yes = ["Yes", "yes"]
choice_try2 = ["Keep trying", "keep trying"]

print("Input \"start\" to start the story")

def introduction():
    print("This is an introduction of the story, ", your_name, "is trying to make this program.")
    print("\n***please input the choices in their full names***")

def conflict_1():
    print("\nProgram meets a problem.")
    print("What is the problem? Crash or Error?")

def conflict_2a():
    print("\nOh noooo, it crashed.")
    print("Why did it crash?", "Wrong code or Problems with app?" )

def conflict_2b():
    print("\nError? Error? Error?")
    print("Continue or Close it?")

def conflict_3a():
    print("\nWrong code...")
    print("Close or Continue?")

def conflict_3b():
    print("\nContinue? Good luck!")
    conflict_4()

def conflict_4():
    print("\n", your_name, "is almost there in completing this program.")
    print("Oh no, ", your_name, " meets problems. Keep trying or Close?")



while True:
    cont = str(input())
    if (cont == "Start") or (cont == "start"):
        introduction()
        conflict_1()
    elif cont in choice_cr: #1st
        conflict_2a()
    elif cont in choice_wrong: #2nd
        conflict_3a()
    elif cont in choice_close: #3rd
        import random
        print(random.choice(endings))
        break
    elif cont in choice_cont: #continue
        conflict_3b()
    elif cont in choice_prob: #problem
        import random
        print(random.choice(endings))
        break
    elif cont in choice_err:
        conflict_2b()
    elif cont in choice_close2:
        print("R U SURE? Yes or No?")
    elif cont in choice_yes:
        import random
        print(random.choice(endings))
        break
    elif cont in choice_no:
        conflict_4()
    elif cont in choice_try2:
        print("FINALLY!", your_name, "finished the program")


