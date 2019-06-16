import sys
import pynput
import keyboard

def MENU(): # first Menu 

    import os

    from ascci import rabbit
    from editor import editor
    from keydetect import keydetect
    from lwsystem import osuser
    from creds import creds

    os.system("clear")
    print "\x1b[0;31m" + "ducky converter/encoder " + "\x1b[0m" + "by"
    CSI="\x1B["
    print " " + CSI + "\x1b[31;5m" + "		  ------------\n                  |DuckyTools|\n                  ------------" + CSI + "0m"
    print "(python2.7)"
    print ("\n")

    userChoice = raw_input("\nMENU :\n\nWhat do you want ?\n\n1) editor for translat many ducky/P4wnP1 keyboard keys \n2) generate payloads for P4wnP1 A.L.O.A with web client interface \n3) test P4wnP1 with a simple keyboard detect key pressed\n4) Creds\n\n99) exit \n\n>>> ") 


    if userChoice == "1":
	editor()

    elif userChoice == "2":
	print "\n"
	os.system("clear")
	osuser()

    elif userChoice == "3":
	keydetect()

    elif userChoice == "4":
	creds()

    elif userChoice == "99":
	rabbit()
	exit()
    else :
        print "\nan error occurred, please try again\n"
	MENU()
#MENU()
