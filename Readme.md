# Jerricha's, a ParagonChat Database App v0.2.0
Introducing: *Jerricha's*, a ParagonChat Database App, something to help us nerdy DB hackers automate our hacking.


##What does *Jerricha's* do?
*Jerricha's* is an command-line tool that simplifies and automates DB costume hacking. *Jerricha's* plugs your /costumesave file straight into your ParagonChat database, without you having to manually query and figure out which fields go where.


##How does it work?
*Jerrichas* batch converts those /costumesave files into a long SQL query (the langauge ParagonChat database uses), and executes it on the ParagonChat database. This assumes that you've already completely designed your costume in Icon.exe, and have /costumesave'd it.

Jerrichas works both at the batch level (replace an entire costume), or at the part level (replace just one part of that costume).


##How do I run Jerrichas?

###From .exe
1. Download [Jerrichas.exe]()
2. Double click on Jerrichas.exe, follow the instructions =)

###From Source

1. Install Python 3 from https://www.python.org/downloads/
2. Install some flavor of git
3.
```
git clone https://github.com/Jerricha/jerrichas
```
4. Run Jerrichas at the commandline with
```python Jerrichas.py```
or
```c:\Python34\python.exe Jerrichas.py```
4. Follow the on-screen instructions


###Cherry-Pick mode
1. Curate your costumefile to include only the parts you want. For example, in [mock_part_mom_trenchcoat](testing/data/mock_part_mom_trenchcoat), this will give you just Mother Mayhem's trenchcoat.
2. Select Cherry-Pick mode from the menu =)

##I'm a hacker / programmer / techie / SQL guru/ curious, why are there so many LoCs? Do I really need this whole program?
No. You are likely only going to be interested in the **Database** class, and the **read_costumepart** function. These do the heavy lifting and expose an API both to the database and /costumesve file. The rest of the program handles validation, tests, and user event threading. >80% of this program is for user interaction.


##Things *Jerrichas* currently does *not* do, but will in the future:
* Updates your proportions. Jerrichas currently just replaces costume parts and sets colors (...ish)
* Changes your characters' names, class, origin, description, battlecry.

###Upcoming features and fixes:
* Bug fixes
* Major code refactoring and documentation, to share with the community
* Compilation into a .exe / .dmg binary
* Better Mac support
* A GUI? Possible web app for user friendliness (and so people don't need to install Python!)
* Full API support
