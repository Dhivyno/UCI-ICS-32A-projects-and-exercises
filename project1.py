from functions_from_ICS_32_a1 import *
import os
from pathlib import *

def error():
    print("ERROR")

def recursive_text_file_search(path, text: str):
    subdir_list = []
    for element in os.listdir(path):
        element_path = Path(os.path.join(path, element))
        if os.path.isdir(element_path):
            subdir_list.append(element_path)
        try:
            if text in element_path.read_text():
                print(element_path)
        except:
            continue
    for subdir in subdir_list:
        recursive_text_file_search(subdir, text)

def text_file_search(path, text: str):
    subdir_list = []
    for element in os.listdir(path):
        element_path = Path(os.path.join(path, element))
        try:
            if text in element_path.read_text():
                print(element_path)
        except:
            continue

def start_first_line():
    first_line = input()
    listing_mode = first_line[0:1]
    recursive = False
    path = os.path.normpath(first_line[2:])
    if not os.path.isdir(path) or (listing_mode != "D" and listing_mode != "R"):
        error()
        start_first_line()
    elif listing_mode =="D":
        list_only(path)
    elif listing_mode == "R":
        recursive = True
        list_recursion(path)
    read_second_line(recursive, path)
    

def read_second_line(recursive: bool, path):
    second_line = input()
    mode = second_line[0:1]
    extra_input = second_line[2:]
    if recursive:
        if second_line == "A":
            list_recursion(path)
        if mode == "N":
            recursion_search(path, extra_input)
        if mode == "E":
            recursion_extension_search(path, extra_input)
        if mode == "T":
            recursive_text_file_search(path, extra_input)

        

if __name__ == "__main__":
    start_first_line()