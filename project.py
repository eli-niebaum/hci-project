playing = True
place = "Start"
key1 = False

print("\n***WELCOME TO DUAL ADVENTURE***")
print("-------------------------------\n")

print("""The aim of the game is to complete the puzzles in the prompts with the use of your wits as well as
your TI-84 Plus CE calculator running the attached program. Good luck!\n""")

while playing:
    if place == "Start":
        print("""
        You open the door to find a dark room slightly lightened by the moonlight from a crack in the ceiling.
        You see a door in the far corner, a closet in the corner opposite to the door, and a sofa slightly off-center
        from everything around it. 
            
        This room seems to be filled with broken clocks, one standing, one hanging, and one sitting on a nightstand next to the sofa. 
        The standing clock shows a time of 11:47, the hanging clock shows 5:22 and the nightstand clock shows 2:59.""")

        while place == "Start":
            print("""    
            What do you investigate?

            Option 1: Corner Door
            Option 2: Corner Closet
            Option 3: Sofa""")

            var = input().lower()
            
            if var == "corner door" or var == "1":
                print("""
            Option 1: You see that the door has a form of rolling passcode lock on it. The lock seems to allot three digits

            Do you wish to open the door?
            Yes or No\n""")
                
                var = input().lower()
                
                if var == "yes":
                    print("\tUse your calculator to find the answer.")
                    print("\tPasscode?")

                    passcode = input()

                    if passcode == "3126":
                        place = "Room2"
                        print("\tYou go to another room...\n")
                        break
                    else:
                        print("\tINCORRECT, TRY AGAIN\n")

                elif var == "no":
                    print("\tYou look to the rest of the room.")
                else:
                    print("\tINVALID INPUT, TRY AGAIN")

            elif var == "corner closet" or var == "2":
                print("""
            Option 2: The closet seems to have a directional keypad needing a combination of movements either up, down, left, or right

            Do you wish to open the closet?
            Yes or No\n""")
                
                var = input().lower()

                if var == "yes":
                    print("\tUse your calculator to find the answer.")
                    print("\tCombination?")

                    passcode = input()

                    if passcode == "1234":
                        print("\tYou find a key")
                        key1 = True
                    else:
                        print("\tINCORRECT, TRY AGAIN")

                elif var == "no":
                    print("\tYou look to the rest of the room.")
                else:
                    print("\tINVALID INPUT, TRY AGAIN")

            elif var == "sofa" or var == "3":
                print("""
            Option 3: You move the sofa to reveal a hatch door with a key latch. A physical key is needed for this door.""")
                
                if key1:
                    print("\tYou open the door.")
                    print("\tYou find a code on the wall: 3126.")
                else:
                    print("\tThe door is locked.")
            else:
                print("\tINVALID INPUT, TRY AGAIN")

    elif place == "Room2":
        print("""
        You enter into a dank and quiet stone blocked cellar. You use the flashlight on your phone to illuminate the room.
        The cellar seems to be not very large, and whoever lived in this house clearly liked wine, as their are over 30 or 
        so casks pressed against the back wall. Each cask of wine has a valve with one of the three materials,
        Bronze, Gold, or Nickel, along with the year the wine was sealed.

        The Bronze casks read \"Barbeito Boal MBV 1802\"

        The Gold casks read \"Madeira 1863\"

        The Nickel casks read \"Terrantez 1797\"
            
        Use your calculator to progress further""")
        
        while place == "Room2":
            var = input("\nCask serial number: ")

            if var == "9346":
                print("""
        You break open the cask marked with the numbers 9346 to feel a lever on the otherside. You pull the lever leading
        to a rumble and movement. You turn around to see the wall at the back of the room turning to be perpendicular...
        revealing a new room.\n""")
                place = "Room3"
                playing = False
            else:
                print("INCORRECT INPUT, TRY AGAIN")