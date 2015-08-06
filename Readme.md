# Jerricha's, a ParagonChat Database App v0.2.0
*Jerricha's*, a ParagonChat Database App, something to help us nerdy DB hackers automate our hacking.

##What does *Jerricha's* do?
*Jerricha's* is an command-line tool that simplifies and automates DB costume hacking. *Jerricha's* plugs your /costumesave file straight into your ParagonChat database, without you having to manually query and figure out which fields go where.


##How does it work?
*Jerrichas* batch converts those /costumesave files into a long SQL query (the langauge ParagonChat database uses), and executes it on the ParagonChat database. This assumes that you've already completely designed your costume in Icon.exe, and have /costumesave'd it.

Jerrichas works both at the batch level (replace an entire costume), or at the part level (replace just one part of that costume).

##How do I run Jerrichas?

###From .exe
1. Download [Jerrichas.exe](https://github.com/Jerricha/jerrichas/raw/master/dist/Jerrichas.exe)
2. Double click on Jerrichas.exe, follow the instructions =)

###From Source (Advanced)

1. Install [Python 3](https://www.python.org/downloads/)
2. Install [git](https://msysgit.github.io/)
3. Clone repo
```
git clone https://github.com/Jerricha/jerrichas
```
4. (Optional) Install [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper-win), create virtualenvironment
```
cd jerrichas
pip install virtualenvwrapper-win
mkvirtualenv jerrichas
setprojectdir .
workon jerrichas
```
4. Run Jerrichas at the commandline with
```python Jerrichas.py```
5. Follow the on-screen instructions

## New Features as of v.0.2.0
##Config file
* Jerrichas will generate a config file, so you can specify your database and costumesave paths. If you ever screw it up, don't worry, Jerrichas will re-generate the config.
* BTW, don't surround your path in quotes, it'll confuse the parser (and let you know)

##Cherry-Pick mode
1. Curate your costumefile to include only the parts you want. For example, in [mock_part_mom_trenchcoat](testing/data/mock_part_mom_trenchcoat), this will give you just Mother Mayhem's trenchcoat.
2. Select Cherry-Pick mode from the menu =)
* Seriously, *don't* select Batch with a cherrypicked file, or you will seriously screw up your costume.

##I'm a poweruser/hacker/programmer/techie, and I can roll my own SQL. Why do I need Jerrichas?
You absolutely can do this manually, as the community has been so far. However, in addition speeding-up and simplifying DB hacking, Jerrichas will feature full API support to the ParagonChat database, so you could build your app / l33t h4x ontop of Jerrichas.


##Things *Jerrichas* currently does *not* do, but will in the future:
* Update your gender! Be careful to choose the right costumefile for the right gender!
* Updates your proportions. Jerrichas currently just replaces costume parts and sets colors (...ish)
* Changes your characters' names, class, origin, description, battlecry, etc.

###Upcoming features:
* ~~Compilation into a .exe~~ (v0.2.0)
* ~~Cherry-pick mode~~ (v0.2.0)
* Full API support for other developers/coders/hackers
* Mac support
* JerrichaQT GUI
