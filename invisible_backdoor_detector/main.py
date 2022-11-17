#!/usr/bin/env python3

from typing import List # To support Python>3.5
import typer
import invisible_backdoor_detector.helper as helper

app = typer.Typer(add_completion=False, context_settings={"help_option_names": ["-h", "--help"]})

# Definition of Bidi Characters array
bidi_characters = ["\u115f","\u1160","\u3164","\uffa0"] #Fillers

def spot_bidi(textfiles: List[str], autoremove: bool):
    helper.log("Trying to spot Bidi characters in your text files...")
    bidi_hex_array = [bidi.encode() for bidi in bidi_characters]
    bidi_textfiles = []
    for filename in textfiles:
        with open(filename, "rb") as file:
            filebytes = file.read()
            for bidi_hex in bidi_hex_array:
                if bidi_hex in filebytes:
                    bidi_textfiles.append(filename)
                    helper.warn(f"There is a Bidi character in {filename} at index {filebytes.index(bidi_hex)} (reading bytes)")
    if len(bidi_textfiles) > 0 and not autoremove:
        helper.log("You may automatically remove all the Bidi characters with the --remove option.")
    elif len(bidi_textfiles) > 0 and autoremove:
        remove_bidi(bidi_textfiles)
    else:
        helper.success("No Bidi character has been found.")

def remove_bidi(textfiles: List[str]):
    helper.log("Removing Bidi characters in your text files...")
    bidi_hex_array = [bidi.encode() for bidi in bidi_characters]
    for filename in textfiles:
        with open(filename, "rb") as input:
            filebytes = input.read()
            for bidi_hex in bidi_hex_array:
                if bidi_hex in filebytes:
                    helper.log(f"Removing Bidi character from {filename} at index {filebytes.index(bidi_hex)} (reading bytes)")
                    clean_filebytes = filebytes.replace(bidi_hex, bytes("", encoding='utf-8'))
                    with open(filename, "wb") as output:
                        output.write(clean_filebytes)
    helper.success("Bidi characters removed.")

@app.command()
def detect(path: str = typer.Argument(..., help="Path of the folder to check"), remove: bool = typer.Option(False, "--remove", "-r", help="Remove the Bidi characters found")):
    helper.banner()
    helper.check_dir(path)
    textfiles = helper.get_utf8_files(path)
    spot_bidi(textfiles, remove)

if __name__ == "__main__":
    app()