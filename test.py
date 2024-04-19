import os
from pathlib import Path

a = Path("C:\\Users\\dhivy\\OneDrive\\Desktop\\UCI_course_assignments\\UCI-ICS-32A-projects-and-exercises\\test.txt")

print(os.path.splitext(a)[1])