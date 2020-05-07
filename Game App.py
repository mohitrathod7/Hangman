from main import *
import time


print("-----------------------------------------HANGMAN GAME BY MOHIT RATHOD-----------------------------------------")

play = True
while True:
    print()
    info = input('''
Press [1] for You v/s Computer
           OR                        
Press [2] for You v/s Friend : ''')
    if info == "1":
        main1()
        print()
        msg = input("Do you want to play again ? ").lower()
        if msg == "yes" or msg == "y":
            play = True
        if msg != "yes" or msg != "y":
            play = False
            time.sleep(1)
            _ = input("Press Enter to Quit")
            time.sleep(1)
            print("GOOD BYE")
            time.sleep(1)
            break

    elif info == "2":
        main2()
        print()
        msg = input("Do you want to play again ? ").lower()
        if msg == "yes" or msg == "y":
            play = True
        if msg != "yes" or msg != "y":
            play = False
            time.sleep(1)
            _ = input("Press Enter to Quit")
            time.sleep(1)
            print("GOOD BYE")
            time.sleep(1)
            break
