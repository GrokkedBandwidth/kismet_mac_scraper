# Kismet MAC Scraper

Simple script for parsing through .kismet files to find which files contain select MACs. 
Meant to save time and processing power for certain intensive programs by only uploading 
.kismet files you actually care about.
## Using Script
The script can be run against a single MAC, a textfile of MACs or a csv of MACs. The script will run against
all .kismets in the current directory unless --dir is used.
### Single MAC
````
python3 scraper.py --mac AA:BB:CC:DD:EE:FF
````
### Textfile
````
python3 scraper.py --textfile Name_of_file.txt
````
### Csv
````
python3 scraper.py --csv Name_of_file.csv
````


