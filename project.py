playing = True
place = "Start"
key1 = False

print("\n***WELCOME TO DUAL ADVENTURE***")
print("-------------------------------\n")

print("""The aim of the game is to complete the puzzles in the prompts with the use of your wits as well as
your TI-84 Plus CE calculator running the attached program. When a prompt mentions using your calculator, it'll
come with a code. Input that code to show the relevant prompt for the puzzle. Good luck!\n""")

print("""One day you received a knock at your door late at night. After cautiously opening your door at your feet stood a box
about a foot in length. The box had a note taped to the top, it read "You have been selected by those of a higher
power to be granted with knowledge and power. Go to the address at the bottom and use what is inside this parcel to
obtain this offering". You open the box to find.... a TI-84 Plus CE calculator, a mighty tool if one knows how to wield it.

Throwing all caution to the wind you immediately throw on some appropriate attire and some shoes and head for the address.
When you arrive you see an ominous run down house, not too large in size, but as it seems, large in history. You make
your way to the front door.\n""")

while playing:
    if place == "Start":
        print("""
        You open the door to find a dark room slightly lightened by the moonlight from a crack in the ceiling.
        You see a door in the far corner, a closet in the corner opposite to the door, and a sofa slightly off-center
        from everything around it. 
            
        This room seems to be filled with broken clocks, one standing, one hanging, and one on a chair next to the sofa. 
        The standing clock shows a time of 11:47, the hanging clock shows 5:22 and the chair clock shows 2:59.""")

        while place == "Start":
            print("""    
            What do you investigate?

            Option 1: Corner Door
            Option 2: Corner Closet
            Option 3: Sofa""")

            var = input().lower()
            
            if var == "corner door" or var == "1":
                print("""
            Option 1: You see that the door has a form of rolling passcode lock on it. The lock seems to allot four digits

            Do you wish to open the door?
            Yes or No\n""")
                
                var = input().lower()
                
                if var == "yes":
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
            Option 2: The closet seems to have a directional keypad needing a combination of movements either up, down, left, or right.

            Do you wish to open the closet?
            Yes or No\n""")
                
                var = input().lower()

                if var == "yes":
                    print("\tUse your calculator to find the answer. Code: 434")
                    print("\tCombination?")

                    passcode = input().lower().replace(" ", "")

                    if passcode == "leftleftuprightdown":
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
            
        Use your calculator to progress further. Code: 681""")
        
        while place == "Room2":
            var = input("\nCask serial number: ")

            if var == "9346":
                print("""
        You break open the cask marked with the numbers 9346 to feel a lever on the otherside. You pull the lever leading
        to a rumble and movement. You turn around to see the wall at the back of the room turning to be perpendicular...
        revealing a new room.\n""")
                place = "Room3"
            else:
                print("INCORRECT INPUT, TRY AGAIN")

    elif place == "Room3":
        print("""
        You enter a room enlightened by a singular large lamp in the corner. In front of you is a table, with a piece of paper. Written on the paper are the words, to receive treasure, you must find where X marks the spot.
        On the wall facing the table is a chalk board. Written on the chalk board are 2 equations:

        y = 3^x
        y = -3(x - 2)

        Next to the paper is a keypad built into the table.

        Use your calculator to continue. Code: 912""")

        while place == "Room3":
            var = input("Passcode: ")

            if var == "7240":
                place = "Final"
            else:
                print("INCORRECT INPUT, TRY AGAIN")

    elif place == "Final":
        print("""
        After entering the numbers into the keypad, the table rumbles and begins to sink. Replacing the table is a set of stairs
        leading down to somewhere suprising well lit compaired to rest of the house so far. You move down further and enter a room.
        The room is quite vast and wide, however is shockingly empty, except for a chest sitting atop a stand. You move towards it
        wondering what is inside. A note lays on top of the chest saying open me. Without hesitation you do as the note says.
        You slowly open the chest to find..... A TI-nSpire CX calculator. This seems like a bad marketing skeem if you ask me.\n""")

        playing = False

print("""
Congratulations! You finished the game. Please visit https://www.ti.com/ for further information on your reward!""")
