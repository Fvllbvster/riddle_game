def play_game():
    print("Welcome, brave adventurer, you have wandered into the Trial of Riddles!")
    print("To make your escape, you must prove your wit. Solve the riddles, or be trapped forever.")


    # -- Room 1 --

    print("\n You find yourself in a poorly lit forest clearing. On the opposite edge you see a typical park bench. On the back is what looks like a memorial plaque.")
    print("You approach to see it reads:")
    print("Your eyes are open and I'm there. Close them. I'm there too. What am I?")

    riddle_1_solved = False
    while not riddle_1_solved:
        answer1 = input("Your answer:").strip().lower()
        if answer1 == "darkness":
            print("The messages glow green as a wind begins whipping through the trees violently and a light fills the clearing.")
            riddle_1_solved = True
        else:
            print("The message begins glowing red and the wind hisses angrily. 'Try a different answer' it screams.")

        
    # -- Room 2 --
    if riddle_1_solved: # only proceed if riddle_1 was solved
        print("\n---")
        print("The light fades and you find yourself on a small island. You look in both directions.")
        print("Completely bare in every direction, it couldn't be more than a half mile in diameter, perfectly flat sand in every direction surrounded by ocean.")
        print("The only thing you see is a small treasure chest, you make your way to it and read the note you find tacked on:")
        print("What's the one place you can be sure you'll never read your name?")

        riddle_2_solved = False
        while not riddle_2_solved:
            answer2 = input("Your answer:").strip().lower()
            if answer2 == "your gravestone":
                print("The chest opens up and you are hit by another flash of light.")
                riddle_2_solved = True
            else:
                print("The chest rattles angrily as if telling you to try again.")

    # -- Room 3 --
    if riddle_2_solved: # only proceed if the second riddle was solved
        print("\n---")
        print("The light from the chest fades and you find yourself standing in a library hall massive beyond comprehension.")
        print("You approach the table in front of you with the note clearly intended for you.")
        print("The note reads, 'What is always in front of you but cannot be seen?'")
        
        riddle_3_solved = False
        while not riddle_3_solved:
            answer3 = input("Your answer:").strip().lower()
            if answer3 == "future":
                print("Congratulations on successfully passing the Trial of Riddles!")
                print("You will shortly be teleported back to whence you came.")
                print("As a reward you are free to visit this library as you please.")
                riddle_3_solved = True
            else:
                print("The pages of the books of the library fluttered themselves in frustration, telling you to think harder.")

        if not riddle_1_solved or not riddle_2_solved or not riddle_3_solved:
            print("\n---")
            print("You were unable to solve all the riddles. The path out remains obscured.")
            print("Game over. Perhaps next time you will come better prepared.")

# start the game
if __name__ == "__main__":
    play_game()
