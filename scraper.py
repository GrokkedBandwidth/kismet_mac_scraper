import sqlite3
import glob
import argparse
import csv

def sql_connection(filelist, directory, target):
    for filename in glob.glob(directory + "*.kismet"):
        con = sqlite3.connect(filename, detect_types=sqlite3.PARSE_DECLTYPES)
        cur = con.cursor()
        cur.execute(f"SELECT devmac FROM 'devices' WHERE devmac='{target}'")
        found_device = str(cur.fetchone())
        if len(found_device) > 4:
            if filename not in filelist:
                print(filename)
                filelist.append(filename)

def scraper(mac):
    filelist = []
    sql_connection(filelist, directory, mac)


def text_deck_scraper(txt_file):
    filelist = []
    with open(txt_file, mode='r') as file:
        for target in file:
            target = target.strip()
            sql_connection(filelist, directory, target)


def csv_deck_scraper(csv_file):
    filelist = []
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for target in reader:
            target = target[0]
            sql_connection(filelist, directory, target)


parser = argparse.ArgumentParser(
    prog="Kismet File Scraper",
    description=".kismet file scraper for quickly identifying what files contain specific MACs."
)
group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument("--dir", "-d",
                    default="./",
                    help="Designates where to run the script. If not designated, script will run in current folder."
                         "Example: --dir /home/user/collection/")

group.add_argument("--mac", "-m",
                    help="Designates the specific MAC you are looking for. Upper or lowercase does not matter",
                    )

group.add_argument("--textfile", "-t",
                    help="Runs the script against a given text file with multiple MACs. One MAC per line is expected "
                         "for ingestion")
group.add_argument("--csvfile", "-c",
                    help="Runs the script against a given csv file with multiple MACs. One MAC per line is expected "
                         "for ingestion")

args = parser.parse_args()
mac = args.mac
mac = str(mac).upper()
textfile = args.textfile
csvfile = args.csvfile
directory = args.dir

if textfile:
    print(f"MACs in {textfile} found in the following .kismet files")
    text_deck_scraper(textfile)
elif csvfile:
    print(f"MACs in {csvfile} found in the following .kismet files")
    csv_deck_scraper(csvfile)
else:
    print(f"{mac} found in the following .kismet files:")
    scraper(mac)
