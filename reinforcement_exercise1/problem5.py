from pathlib import *

def lines_of_code(path: Path):
    count = 0
    with open(path, "r") as f:
        for line in f:
            code = False
            for char in ''.join((''.join(line.strip().split(" "))).split("\t")):
                if char == "#":
                    break
                elif char != " ":
                    code = True
                    break
            if code:
                count += 1
    return (count)

if __name__ == "__main__":
    lines = lines_of_code("C:\\Users\\dhivy\\OneDrive\\Desktop\\UCI_course_assignments\\UCI-ICS-32A-projects-and-exercises\\reinforcement_exercise1\\problem2.py")
    print("There are " + str(lines) + " lines of code in that python file")