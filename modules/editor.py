import os
def editor(): # tool editor function

    from ascci import rabbit
    from editor import editor
    from keydetect import keydetect
    from lwsystem import osuser
    from creds import creds
    from menu import MENU

    liste = []
    os.system("clear")
    print ("translate a ducky script keyboard keys into a keyboard keys adapted to the web interface of P4wnP1 A.L.O.A.\n\nput a ducky script keyboard keys and press enter to add another ducky script,\npress" +"\x1b[0;31m" + " CTRL c " + "\x1b[0m" + "when you are finish\n\nESC, GUI r, ENTER, STRING, REM, ALT, CTRL, TAB, LEFT, RIGHT, UP, DOWN, F1, F2, DELETE, CAPSLOCK, NUMLOCK, HOME, END, BREAK \n") #\n\n========================\npress ENTER for continue\n========================\n")

    while 1== 1:
        try:
	    liste.append(raw_input("\x1b[0m"+""))
        except KeyboardInterrupt:
            print("\n")
            for l in liste:
                if l == "GUI r": 		# GUI r
                    print('press(\"GUI r\")')	# press("GUI r")

                elif l[:3] == "REM":		# REM
                    print "//"+str(l[3:]) 	# //

	        elif  l[:5] == "DELAY":			# DELAY
	    	    print "delay("+str(l[6:])+str(")")  # delay()

	        elif l[:6] == "STRING":			  	# STRING
		    print "type(\""+str(l[7:])+str("\")") 	# type("")

	        elif l == "ENTER":		# ENTER
		    print "press(\"ENTER\")"	# type("\n") or press("ENTER")

                elif l == "SHIFT":		# SHIFT
                    print "press(\"SHIFT\")"	# press("SHIFT")

	        elif l == "ALT":		# ALT
	       	    print "press(\"ALT\")"	# press("ALT")

                elif l == "CAPSLOCK":			# CAPSLOCK
                    print "press(\"CAPSLOCK\")"		# press("CAPSLOCK")

                elif l == "NUMLOCK":		# NUMLOCK
                    print "press(\"NUMLOCK\")"	# press("NUMLOCK")

                elif l == "HOME":		# HOME
                    print "press(\"HOME\")"	# press("HOME")

                elif l == "END":	# END
                    print "press(\"END\")"	# press("END")

	        elif l == "CTRL":		# CTRL
	       	    print "press(\"CTRL\")"	# press("CTRL")

                elif l == "ESC": 		# ESC or ESCAPE
                    print "press(\"ESC\")"	# press("ESC")

                elif l == "ESCAPE":                # ESC or ESCAPE
                    print "press(\"ESC\")"      # press("ESC")

                elif l == "TAB":		# TAB
                    print "press(\"TAB\")"	# press("TAB")

                elif l == "BREAK":		# BREAK
                    print "press(\"BREAK\")"	# press("BREAK")

		elif l == "DELETE":		# DELETE
		    print "press(\"DELETE\")"	# press("DELETE")

	        elif l == "UP":		 	# UP
		    print "press(\"UP\")"	#press("UP")

	        elif l == "UPARROW":		# UPARROW
		    print "press(\"UP\")"	# press("UP")

	        elif l == "DOWN":		#DOWN
		    print "press(\"DOWN\")"	#press("DOWN")

                elif l == "DOWNARROW":		# DOWNARROW
                    print "press(\"DOWN\")"	# press("DOWN")

                elif l == "RIGHT":		# RIGHT
                    print "press(\"RIGHT\")"	# press("RIGHT")

                elif l == "RIGHTARROW":		# RIGHTARROW
                    print "press(\"RIGHT\")"	# press("RIGHT")

                elif l == "LEFTARROW": 		# LEFTARROW
                    print "press(\"LEFT\")"	# press("LEFT")

                elif l == "LEFT":          	# LEFT
                    print "press(\"LEFT\")"     # press("LEFT")

                elif l == "F1":			# F1
                    print "press(\"F1\")"	# press("F1")

                elif l == "F2":			# F2
                    print "press(\"F2\")"

                elif l == "F3":			# F3
                    print "press(\"F3\")"

                elif l == "F4":			# F4
                    print "press(\"F4\")"

                elif l == "F5":			# F5
                    print "press(\"F5\")"

                elif l == "F6":			# F6
                    print "press(\"F6\")"

                elif l == "F7":			# F7
                    print "press(\"F7\")"

                elif l == "F8":			# F8
                    print "press(\"F8\")"

                elif l == "F9":			# F9
                    print "press(\"F9\")"

                elif l == "F10":		# F10
                    print "press(\"F10\")"

                elif l == "F11":		# F11
                    print "press(\"F11\")"

                elif l == "F12":		# F12
                    print "press(\"F12\")"

            menu = raw_input("\n\n\nWhat do you want now ?\n\n1) convert another\n2) back to menu\n3) exit\n\n> ") # second menu
	    if menu == "1":
		editor()

            elif menu == "2":
		os.system("clear")
		MENU()
	    elif menu == "3":
		rabbit()
		exit()
            break

