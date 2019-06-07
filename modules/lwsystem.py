from pwindows import windows
from plinux import linux

def osuser():	# OS - WINDOWS / LINUX
    os = raw_input("choose the os : \n\n1) Windows\n2) Linux Gnome desktop environment\n\n> ")

    if os == "1":
	windows()

    elif os == "2":
	linux()
