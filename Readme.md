Introducing: *Jerricha's*, a ParagonChat Database Utility, something to help us nerdy DB hackers automate our hacking.

**What does *Jerricha's* do?**
*Jerricha's* is an command-line tool that simplifies and automates DB costume hacking. *Jerricha's* plugs your /costumesave file straight into your ParagonChat database, without you having to manually query and figure out which fields go where.


**How does it work?**
*Jerrichas* batch converts those /costumesave files into a long SQL query (the langauge ParagonChat database uses), and executes it on the ParagonChat database. This assumes that you've already completely designed your costume in Icon.exe, and have /costumesave'd it.

Jerrichas works at the batch level. If you're just interested in cherry-picking costume parts, Jerrichas is (currently) not the tool for this.


**How do I get it running?**
1. Download Jerrichas.py
2. Install Python 3 from https://www.python.org/downloads/
3. Run Jerrichas at the commandline with
```
python Jerrichas.py
```
or
```
c:\Python34\python.exe Jerrichas.py
```
4. When you run the program out of the box, you'll get an instructions screen. You need to set two global variables, PARAGON_CHAT_DB and COSTUME_FILE, and you're ready to go.


I'm a hacker / programmer / techie / SQL guru/ curious, why are there so many LoCs? Do I really need this whole program?**
No. You are likely only going to be interested in the **Database** class, and the **read_costumepart** function. These do the heavy lifting and expose an API both to the database and /costumesve file. The rest of the program handles validation, tests, and user event threading. >80% of this program is for user interaction.


**Things *Jerrichas* currently does *not* do, but will in the future:**
* Updates your proportions. Jerrichas currently just replaces costume parts and sets colors (...ish)
* Changes your characters' names, class, origin, description, battlecry.
* Cherrypicking - choose which exact costume part you want, without replacing the rest of the costume

**Upcoming features and fixes:**
* Bug fixes
* Major code refactoring and documentation, to share with the community
* Compilation into a .exe / .dmg binary
* Better Mac support
* A GUI? Possible web app for user friendliness (and so people don't need to install Python!)
* Full API support
