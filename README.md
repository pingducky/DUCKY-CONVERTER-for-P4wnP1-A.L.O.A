# DUCKY-CONVERTER-for-P4wnP1-A.L.O.A

## UPDATE

Simple support to convert a ducky script keyboard language into a keyboard language for P4wnP1 A.L.O.A. and generate payloads for the web interface of P4wnP1 A.L.O.A.

![menu2](https://user-images.githubusercontent.com/47247782/59147177-c61a0700-89f8-11e9-8e80-4c1ef1781085.png)
##  1\) Editor Ducky script / P4wnP1 A.L.O.A

![editor2](https://user-images.githubusercontent.com/47247782/59147170-bc909f00-89f8-11e9-859e-72de33597f09.png)

Enter a Ducky script keyboard keys and press enter to validate a new line, press CTRL c to show the result


## 2\) generate payloads for P4wnP1 A.L.O.A for the web client interface

![payloadwindows](https://user-images.githubusercontent.com/47247782/59147178-c914f780-89f8-11e9-8059-9c455cab473f.png)

choose the operating system you want to attack, select the payload to configure and generate, enter the layout keyboard like : fr, de, us ..


Put the delay between each instruction, this corresponds to the "delay()" value of p4wnp1.

Some payloads require that the ums of P4wnP1 aloa be enabled

by default the ums name of P4wnP1 is README but it only does a few mo which is annoying if document extraction requires multiple files to be extracted.

<br>
to create a new disk of P4wnP1: 

```
cd /usr/local/P4wnP1/helper
./genimg -i -s 500 -o newums -l umsname
```

the fr layout is buger, it doesn't support the "|" character which is annoying to make pipelines on a hid powershell attack

we can however bypass the problem in layout fr:
```
layout('us')
<br>
press("RIGHT_ALT 6")
<br>
layout('fr')
```
So I added payloads in layout fr with which the problem was fixed
<br>
when you have finished the configs, the payload will be and saved as **Output/ folder** and it displayed this :

![SORTIT](https://user-images.githubusercontent.com/47247782/59147179-cb775180-89f8-11e9-90f8-787243ebb054.png)
## 3\) test P4wnP1 

![KEYDETECT](https://user-images.githubusercontent.com/47247782/59147175-c31f1680-89f8-11e9-8ef6-71a039842507.png)
<br>simple python keyboard detect key press **to test P4wnP1**

## 4) Credits
Thanks 
       [@mame82 for P4wnP1](https://twitter.com/mame82)
       <br>
       [@Seytonic for his good explanations and tutorials on P4wnP1](https://twitter.com/Seytonic)
       <br>
       [@BeBoxoS for share his projects and ideas](https://twitter.com/BeBoXoS)
       <br>

## Installation

![install2](https://user-images.githubusercontent.com/47247782/59147174-bf8b8f80-89f8-11e9-9288-ff099d72c178.png)

**to install :**

```
git clone https://github.com/DuckyTools/DUCKY-CONVERTER-for-P4wnP1-A.L.O.A

cd DUCKY-CONVERTER-for-P4wnP1-A.L.O.A

pip install -r requirements.txt

python ducky-converter_P4wnP1-ALOA.py
```
