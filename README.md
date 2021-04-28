# Vega Strike Save Converter
Vega Strike Save Converter is a command-line tool written in Python that converts Vega Strike's saved games from the old text encoding (cp1252 up to game version 0.5.x) to the currently used utf-8 (game version 0.6.x or newer).


## Usage
Running saveconverter.py with -h or --help will tell you this:

usage: saveconverter.py [-h] -d DIR [-p PATTERN] -b BACKUP_DIR [-e ENCODING]

optional arguments:
  -h, --help            show this help message and exit

  -d DIR, --dir DIR     directory of files to convert (default: None)

  -p PATTERN, --pattern PATTERN
                        optional pattern of files to convert, e.g. -p "Bounty*" (used with -d) 		                        (default: *)

  -b BACKUP_DIR, --backup_dir BACKUP_DIR backup directory for the original files (default: None)

  -e ENCODING, --encoding ENCODING encoding of the text files (default: cp1252)


## Requirements
At the current version, Vega Strike Save Converter only relies on core modules, and it runs on Python 3.X; the only requirement is Python itself.
	