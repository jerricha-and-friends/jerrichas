# Jerricha's Changelog
## 0.3.0 (08-08-2015)
### Bug-fixes
* Fixed bug (#6) whereby secondary colors weren't being updated in the DB.
### API
* Refactored Costumesave and Database classes into jerrichas.CostumeCSV and jerrichas.ParagonChatDB


## 0.2.1 (08-07-2015)
### UI
* Updated main mode display to mark Cherry-pick mode as "advanced"
* Config file and menu have a link to Jerrichas Github page.
* New guide to whole DB hacking: [The Ultimate Guide "DBing your Costume" Using Jerrichas](./guide-to-jerrichas.md)

### Binary
* ~Fleshed out compiling process; versioning metadata.~ [Nope](https://stackoverflow.com/questions/31290641/how-do-i-use-pywintypes-unicode). pywin.Unicode doesn't play well with py3k's native unicode type

## v0.2.0 (08-05-2015)
### Features
* New config file user interface for specifying the DB and costumefile. Re-generates when corrupted
* Cherry-pick modes., allowing users to just replace a few costumeparts into a costume
* Compiles to .EXE, runs in windowed mode without autoquitting.

### Bugfixes
* Batch costume replace no longer replaces the wrong costume id (H/T to Pengy!)

### API
* new Costumesave class
