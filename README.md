# DUCKY-CONVERTER-for-P4wnP1-A.L.O.A

## UPDATE

Simple support to convert a ducky script keyboard language into a keyboard language for P4wnP1 A.L.O.A. and generate payloads for the web interface of P4wnP1 A.L.O.A.

![menu](https://user-images.githubusercontent.com/47247782/59144500-56e0ea80-89d9-11e9-9838-cca199a155b8.png)

##  1\) Editor Ducky script / P4wnP1 A.L.O.A

![editeur](https://user-images.githubusercontent.com/47247782/59144621-8b08db00-89da-11e9-92a8-c7dc4143783f.png)

Enter a Ducky script keyboard keys and press enter to validate a new line, press CTRL c to show the result


## 2\) generate payloads for P4wnP1 A.L.O.A for the web client interface

![payload-windows](https://user-images.githubusercontent.com/47247782/59144934-361a9400-89dd-11e9-8569-60121facdbd2.png)


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

![sortit](https://user-images.githubusercontent.com/47247782/59145522-5d755f00-89e5-11e9-924f-8805f2326394.png)

## 3\) test P4wnP1 

![test-keyboard](https://user-images.githubusercontent.com/47247782/59145516-4cc4e900-89e5-11e9-95aa-5837b10a2924.png)
<br>simple python keyboard detect key press **to test P4wnP1**

## 4) Credits
Thanks 
       [@mame82 for P4wnP1](https://twitter.com/mame82)
       <br>
       [@Seytonic for his goold explanations and tutorials on P4wnP1](https://twitter.com/Seytonic)
       <br>
       [@BeBoxoS for share his projects and ideas](https://twitter.com/BeBoXoS)
       <br>

## Installation

![install](https://user-images.githubusercontent.com/47247782/59144498-4fb9dc80-89d9-11e9-82b9-253093eb40b4.png)

**to install :**

```
git clone https://github.com/DuckyTools/DUCKY-CONVERTER-for-P4wnP1-A.L.O.A

cd DUCKY-CONVERTER-for-P4wnP1-A.L.O.A

pip install -r requirements.txt

python ducky-converter_P4wnP1-ALOA.py
```
