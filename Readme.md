# Jerricha's, a ParagonChat Database App v0.2.0
*Jerricha's*, a ParagonChat Database App, something to help us nerdy DB hackers automate our hacking.
# Table of Contents
<!-- TOC depth:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Jerricha's, a ParagonChat Database App v0.2.0](#jerrichas-a-paragonchat-database-app-v020)
- [Table of Contents](#table-of-contents)
	- [What does *Jerricha's* do?](#what-does-jerrichas-do)
	- [How does it work?](#how-does-it-work)
	- [How do I run Jerrichas?](#how-do-i-run-jerrichas)
		- [From .exe](#from-exe)
		- [From Source (Advanced)](#from-source-advanced)
	- [New Features as of v.0.2.0](#new-features-as-of-v020)
		- [Config file](#config-file)
		- [Cherry-Pick mode](#cherry-pick-mode)
	- [I'm a poweruser/hacker/programmer/techie, and I can roll my own SQL. Why do I need Jerrichas?](#im-a-poweruserhackerprogrammertechie-and-i-can-roll-my-own-sql-why-do-i-need-jerrichas)
	- [Things *Jerrichas* currently does *not* do, but will in the future:](#things-jerrichas-currently-does-not-do-but-will-in-the-future)
	- [Upcoming features](#upcoming-features)
<!-- /TOC -->

## What does *Jerricha's* do?
*Jerricha's* is an shell app that simplifies and automates [DB costume hacking](http://www.cohtitan.com/forum/index.php/topic,11076.0.html).

*Jerricha's* imports costumesave files straight into your ParagonChat database, without you having to manually query and figure out which fields go where.

I also wrote a complete newbie and idiot-proof guide to DB hacking with Jerrichas: [The Ultimate Guide "DBing your Costume" Using Jerrichas](docs/guide-to-jerrichas.md)

## How does it work?
*Jerrichas* batch converts those costumesave files into a long SQL query (the langauge ParagonChat database uses), and executes it on the ParagonChat database. This assumes that you've already completely designed your costume in Icon.exe, and have /costumesave'd it.

Jerrichas works both at the batch level (replace an entire costume), or at the part level (replace just one part of that costume).

## I'm a total newbie to DBing and I have no idea what you just said. Can you just take me to the thing?
YES, just read this: [The Ultimate Guide "DBing your Costume" Using Jerrichas](docs/guide-to-jerrichas.md)

## How do I run Jerrichas?

### From .exe
1. Download [Jerrichas.exe](https://github.com/Jerricha/jerrichas/raw/master/dist/Jerrichas.exe)
2. Double click on Jerrichas.exe, follow the instructions =)

### From Source (Advanced)

1. Install [Python 3](https://www.python.org/downloads/)
2. Install [git](https://msysgit.github.io/)
3. Clone the repo
```
git clone https://github.com/Jerricha/jerrichas
```
4. (Optional) Install [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper-win), a create virtualenvironment
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
### Config file
* Jerrichas will generate a config file, so you can specify your database and costumesave paths. If you ever screw it up, don't worry, Jerrichas will re-generate the config.
* BTW, don't surround your path in quotes, it'll confuse the parser (and let you know)

### Cherry-Pick mode
1. Curate your costumefile to include only the parts you want. For example, in [mock_part_mom_trenchcoat](testing/data/mock_part_mom_trenchcoat), this will give you just Mother Mayhem's trenchcoat.
2. Select Cherry-Pick mode from the menu =)
* Seriously, *don't* select Batch with a cherrypicked file, or you will seriously screw up your costume.

## I'm a poweruser/hacker/programmer/techie, and I can roll my own SQL. Why do I need Jerrichas?
You absolutely can do this manually, as the community has been so far. However, in addition speeding-up and simplifying DB hacking, Jerrichas will feature full API support to the ParagonChat database, so you could build your app / l33t h4x ontop of Jerrichas.


## Things *Jerrichas* currently does *not* do, but will in the future:
* Update your gender! Be careful to choose the right costumefile for the right gender!
* Updates your proportions. Jerrichas currently just replaces costume parts and sets colors (...ish)
* Changes your characters' names, class, origin, description, battlecry, etc.

## Upcoming features
* ~~Compilation into a .exe~~ (v0.2.0)
* ~~Cherry-pick mode~~ (v0.2.0)
* Full API support for other developers/coders/hackers
* Mac support
* JerrichaQT GUI
* Automated testing
