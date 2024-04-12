from functions_from_ICS_32_a1 import *
import os

def read_first_line():
    first_line = input()
    listing_mode = first_line[0:1]
    path = os.path.normpath(first_line[2:])
    if not os.path.isdir(path) or (listing_mode != "D" and listing_mode != "R"):
        error()
        read_first_line()
    else:
        return(listing_mode, path)

def read_second_line():
    second_line = input()
    