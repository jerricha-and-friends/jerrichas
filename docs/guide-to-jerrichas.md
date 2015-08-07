# The Ultimate Guide "DBing your Costume" Using Jerrichas
By Jerricha (jerricha@chat.cohtitan.com)

<!-- TOC depth:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [The Ultimate Guide "DBing your Costume" Using Jerrichas](#the-ultimate-guide-dbing-your-costume-using-jerrichas)
- [What is "DBing your costume"?](#what-is-dbing-your-costume)
- [The Idiot-Proof Guide to using Jerrichas](#the-idiot-proof-guide-to-using-jerrichas)
	- [Step 1: Run Icon.exe with the -n flag](#step-1-run-iconexe-with-the-n-flag)
	- [Step 2: Design Your Costume](#step-2-design-your-costume)
	- [Step 3: Saving a costumesave file](#step-3-saving-a-costumesave-file)
	- [Step 4: Configure Jerrichas](#step-4-configure-jerrichas)
	- [Step 5: Re-Run Jerrichas](#step-5-re-run-jerrichas)
- [(Advanced) How to use Cherry-Pick Mode](#advanced-how-to-use-cherry-pick-mode)
- [A few caveats](#a-few-caveats)
<!-- /TOC -->

# What is "DBing your costume"?
Want to wear that sassy Sibyl's toga dress from Cimmoria? How about Mother Mayham's badass trenchcoat? Or Positron's helmet? What about making yourself look like a 5th Column Vampyr? Welcome to the magical world of DBing your costume.

What people are calling "DBing" let's you wear costume parts that you don't have access as a normal player in ParagonChat. That's because these costume parts are historically restricted to NPCs and the CoX devs, and you can't access them with an ordinary visit to the tailor.

This guide, aimed at being idiot-proof, will walk you through the entire process of designing your costume in Icon.exe, and importing your new DB'd costume into ParagonChat using **Jerrichas**.

# The Idiot-Proof Guide to using Jerrichas

## Step 1: Run Icon.exe with the -n flag
*(If you already know how to pass flags to executables, goto Step 2)*
1. Open up notepad, and add the following line:
```
icon.exe -n
```
2. Hit save, and locate the root of your City of Heroes install directory. If you're using Tequila, you can find where this directory is located in **Options > Install Path**
3. Save the file as **icon-debug.bat**. This is an MS-DOS script that will unlock all NPC costume parts.
  * Note, you may have permission / UAC issues when saving. One way to resolve this is by opening up notepad.exe in Administrator mode
4. Double-click on **icon-debug.bat**, and wait for **Icon** to load.

## Step 2: Design Your Costume
1. When **Icon** loads, you're taken right to the character creation screen. In the costume tab, you'll have access to a **ton** of new NPC parts! Have fun designing your costume!
  * You can also **save your costume** as an ordinary *.costume* file by clicking "save costume." This is useful for future reference, but you will only be able to open it up in this character creation screen with NPC mode activated. You **cannot** use this save file with Jerrichas.
2. When you're done designing, enter the game!

## Step 3: Saving a costumesave file
1. After your character has loaded into the game, type this into your chat:
```
/access_level 9
```
This will give you access to the CoX console.
2. Press ` (the tilda key - on US keyboards, usually located above your tab key), and type into the CoX console window:
```
costumesave my_awesome_costume
```
Of course, you can name your costumesave file it whatever you want, as long as you remember it.
  * *NOTE*: costumesave file is usually saved in your "City of Heroes\Data" folder

3. This is your **costumesave** file that stores all the data about the costume you just made. If you're curious, it's in a format that we call **CSV**, or comma-separated-values. Think of it like a spreadsheet without the column headers.


## Step 4: Configure Jerrichas
1. Download and save [Jerrichas.exe](../dist/Jerrichas.exe).
2. Double-Click on **Jerrichas.exe** and read the on-screen instructions (there may be some overlap with this guide.)
  * *NOTE*: Jerrichas is a console app, and might take a few seconds to load. Please be patient, it's not broken!
3. *Configuration*: Open **jerrichas.ini** that **Jerrichas.exe** *just* created, and set **COSTUME_FILE** to the path to your **costumefile** you made. For example, my jerrichas.ini looks like this:
```
[Jerrichas]
COSTUME_FILE = c:\Games\City of Heroes\Data\my_awesome_costume
PARAGON_CHAT_DB = %(APPDATA)s\Paragon Chat\Database\ParagonChat.db
```
  * **NOTE**: You usually don't have to change **PARAGON_CHAT_DB**, unless you have some funky Windows settings set.
  * *Jerrichas is Smart!*: If you ever screw up your **jerrichas.ini** config file, delete one of the values, or add garbage, just run Jerrichas.exe again -- Jerrichas will re-create a new one.

## Step 5: Re-Run Jerrichas
1. **CLOSE** ParagonChat completely if you have it open. This means the CoX client and the login screen.
2. **BACKUP** your **ParagonChat.db**. It's usually located at:
```
%APPDATA\Paragon Chat\Database\ParagonChat.db
```
3. Assuming we have the config file set up correctly, and all of the paths validate, Jerrichas will take you to the menu screen.
  * *Jerrichas is Smart!*: If the path doesn't validate, Jerrichas will let you know. Go back and fix your costumesave path.
4. Select **Batch Mode**.
5. Choose your character, then your costume number. Make sure you pick the character that corresponds to your costume's gender.
  * *Note*: Costume indices begin at 0 and end in 9. 0th is the topmost-left, and 9th is the bottom-most right.
  * Be sure to read the [caveats](#a-few-caveats).
6. Choose Yes to confirm. You're done. Enjoy!

# (Advanced) How to use Cherry-Pick Mode
1. Open up your **costumesave** file in your favorite text editor.
2. Delete every line except for the specific costume parts you want. Each line is it's own costume part.
  * If you need help identifying which part is which, I recommend the post [List of NPC Costume Pieces and Database key](http://www.cohtitan.com/forum/index.php/topic,11165.0.html) by [Noyjitat](http://www.cohtitan.com/forum/index.php?action=profile;u=4173)
3. Run Jerrichas, and choose **Cherry-Pick mode**.
  * **WARNING**: DO NOT choose Batch Mode with a cherry-picked file. You'll screw up your costume bad.

# A few caveats
As of Jerrichas v0.2.0, Jerrichas cannot:
  * detect what gender your costume
  * cannot change your costume proportions
So make sure your original ParagonChat character costume has the right gender and proportions before you replace it with a costumesave file.
