'''
Author: Angelo Delicato
Email: angelo.delicato@secsi.io
'''

import sys
import os
import argparse
import glob
from art import text2art

# Definition of Bidi Characters array
bidi_characters = ["\u115f","\u1160","\u3164","\uffa0"] #Fillers

def main():
    sexy_intro()
    args = parse_args()
    args.func(args)
    textfiles = get_utf8_files(args.path)
    spot_bidi(textfiles, args.remove)

# Check if the path is a folder
def check_dir(args):
    if not os.path.isdir(args.path):
        print("This is not a folder, exiting...")
        sys.exit(-1)

def get_utf8_files(path):
    print("Getting valid text files...")
    textfiles = []
    for filename in glob.iglob(path + '**/**', recursive=True):
        if os.path.isfile(filename):
            with open(filename, encoding="utf-8", errors="strict") as f:
                try:
                    f.readline()
                    textfiles.append(filename)
                except UnicodeDecodeError:
                    print("{filename} is not a valid text file, discarding.".format(filename=filename))
    print("")
    return textfiles

def spot_bidi(textfiles, autoremove):
    print("Trying to spot Bidi characters in your text files...")
    bidi_hex_array = [bidi.encode() for bidi in bidi_characters]
    bidi_textfiles = []
    for filename in textfiles:
        with open(filename, "rb") as file:
            filebytes = file.read()
            for bidi_hex in bidi_hex_array:
                if bidi_hex in filebytes:
                    bidi_textfiles.append(filename)
                    print("[ATTENTION] There is a Bidi character in {filename} at index {index} (reading bytes)".format(filename=filename, index=filebytes.index(bidi_hex)))
    if len(bidi_textfiles) > 0 and not autoremove:
        print("You may automatically remove all the Bidi characters with the --remove option.")
    elif len(bidi_textfiles) > 0 and autoremove:
        remove_bidi(bidi_textfiles)
    else:
        print("No Bidi character has been found.")

def remove_bidi(textfiles):
    print("Removing Bidi characters in your text files...")
    bidi_hex_array = [bidi.encode() for bidi in bidi_characters]
    for filename in textfiles:
        with open(filename, "rb") as input:
            filebytes = input.read()
            for bidi_hex in bidi_hex_array:
                if bidi_hex in filebytes:
                    print("Removing Bidi character from {filename} at index {index} (reading bytes)".format(filename=filename, index=filebytes.index(bidi_hex)))
                    clean_filebytes = filebytes.replace(bidi_hex, bytes("", encoding='utf-8'))
                    with open(filename, "wb") as output:
                        output.write(clean_filebytes)

# Print out a Sexy intro
def sexy_intro():
    secsi_art=text2art("SecSI",font='big')
    print()
    print(secsi_art, end="")
    print("unicode-bidi detector - secsi.io")

def parse_args():
    parser = argparse.ArgumentParser(prog="unicode-bidi-detector", description='Spot Unicode Bidi characters in your codebase.')
    subparsers = parser.add_subparsers()
    path_parser = subparsers.add_parser('path')
    path_parser.add_argument("path", help="The path to your source code")
    path_parser.set_defaults(func=check_dir)
    parser.add_argument("--remove", help="Wheter automatically remove or not the spotted Bidi characters", action='store_true')
    args = parser.parse_args()
    # Check args
    return args

if __name__ == "__main__":
    main()