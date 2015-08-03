Hey guys :-)

After spending all day Sunday writing my app Jerrichas, I finally have a working prototype!
Introducing: [i]Jerricha's[/i], a ParagonChat Database Utility, something to help us nerdy DB hackers automate our hacking.

[b]What does [i]Jerricha's[/i] do?[/b]
[i]Jerricha's[/i] is an command-line tool that simplifies and automates DB costume hacking. [i]Jerricha's[/i] plugs your /costumesave file straight into your ParagonChat database, without you having to manually query and figure out which fields go where.


[b]How does it work?[/b]
[i]Jerrichas[/i] batch converts those /costumesave files into a long SQL query (the langauge ParagonChat database uses), and executes it on the ParagonChat database. This assumes that you've already completely designed your costume in Icon.exe, and have /costumesave'd it.

Jerrichas works at the batch level. If you're just interested in cherry-picking costume parts, Jerrichas is (currently) not the tool for this.


[b]How do I get it running?[/b]
First, you need Python 3. Next, you run Jerrichas at the commandline with "python Jerrichas.py" or "c:\Python34\python.exe Jerrichas.py". When you run the program out of the box, you'll get an instructions screen. You need to set two global variables -- one to your ParagonChat.db path, and another to your , and you're ready to go.


[b]I'm a hacker / programmer / techie / SQL guru/ curious, why are there so many LoCs? Do I really need this whole program?[/b]
No. You are likely only going to be interested in the [b]Database[/b] class, and the [b]read_costumepart[/b] function. These do the heavy lifting and expose an API both to the database and /costumesve file. The rest of the program handles validation, tests, and user event threading. >80% of this program is for user interaction.


[b]Things [i]Jerrichas[/i] currently does [i]not[/i] do, but will in the future:[/b]
* Updates your proportions. Jerrichas currently just replaces costume parts and sets colors (...ish)
* Changes your characters' names, class, origin, description, battlecry.
* Cherrypicking - choose which exact costume part you want, without replacing the rest of the costume

[b]Upcoming features and fixes:[/b]
* Bug fixes
* Major code refactoring and documentation, to share with the community
* Compilation into a .exe / .dmg binary
* Better Mac support
* A GUI? Possible web app for user friendliness (and so people don't need to install Python!)
* Full API support
