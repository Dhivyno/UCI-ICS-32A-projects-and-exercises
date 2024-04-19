from functions_from_ICS_32_a1 import *
import os
from pathlib import *

def error() -> None:
    print("ERROR")

def print_list(array) -> None:
    for item in array:
        print(item)

# function for listing everything in source directory
def listing(path: Path, recursive: bool, files: list[Path]) -> list[Path]:
    subdir_list = []
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in os.listdir(path):
        file_path = Path(path, content)
        if os.path.isdir(file_path) and recursive:
            subdir_list.append(file_path)
        elif os.path.isfile(file_path):
            files.append(file_path)
    for subdir in subdir_list:
        listing(subdir, recursive, files)
    return files

def remove_unwanted_files(command: str, files: list[Path], extra_input=None) -> list[Path]:
    new_files = []
    if command == "A":
        return files
    for file in files:
        if command == "N" and os.path.basename(file) == extra_input:
            new_files.append(file)
        elif command == "E" and (os.path.splitext(file)[1] == extra_input or os.path.splitext(file)[1][1:] == extra_input):
            new_files.append(file)
        elif command == "T" and extra_input in file.read_text():
            new_files.append(file)
        elif command == "<" and os.path.getsize(file) < int(extra_input):
            new_files.append(file)
        elif command == ">" and os.path.getsize(file) > int(extra_input):
            new_files.append(file)
    return new_files
    
def action(command: str, files: list[Path]) -> None:
    for file in files:
        path = Path(file)
        if command == "F":
            try:
                sentences = path.read_text().split("\n")
                print(sentences[0])
            except:
                print("NOT TEXT")
        elif command == "D":
            new_path = str(file) +".dup"
            with open(new_path, "w"):
                pass
        elif command == "T":
            file.touch(exist_ok=True)

def start_first_line() -> None:
    first_line = input()
    listing_mode = first_line[0:1] # gets the listing mode from input
    recursive = False # sets recursive to false until mode is found to be "R"
    path = os.path.normpath(first_line[2:]) # gets the path of the directory from the input and makes it a Path object
    if not os.path.isdir(path) or (listing_mode != "D" and listing_mode != "R") or len(path) <= 1:
        error()
        start_first_line()
    else:
        if listing_mode == "R": # sets recursive to be true when mode is "R"
            recursive = True
        interesting_files = listing(path, recursive, files=[])
        print_list(interesting_files)
        read_second_line(interesting_files)

def read_second_line(files: list[Path]) -> None:
    second_line = input() 
    mode = second_line[0:1] # takes input for second line and splits into mode and extra input
    extra_input = second_line[2:]
    interesting_files = remove_unwanted_files(mode, files, extra_input)
    print_list(interesting_files)
    if mode not in ["A", "N", "E", "T", "<", ">"] or (mode != "A" and len(extra_input) < 1):
        error()
        read_second_line(files)
    else:
        read_third_line(interesting_files)

def read_third_line(files: list[Path]) -> None:
    third_line = input()
    if third_line not in ["F", "D", "T"]:
        error()
        read_third_line(files)
    else:
        action(third_line, files)


if __name__ == "__main__":
    start_first_line()