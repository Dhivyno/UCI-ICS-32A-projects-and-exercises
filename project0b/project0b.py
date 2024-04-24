# a0.py

# Replace the following placeholders with your information.

# Dhivyesh Kanagasabai
# EMAIL
# STUDENT ID

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# asks user for number input
number = int(input())

def downward_block(num):
    # starts the first 2 lines as they are not part of the loopable part of the structure
    print("+-+")
    print("| |")
    # draws the middle part (loopable part) of the structure
    for i in range(num-1):
        print(" "*2*(i) + "+-+-+")
        print(" "*2*(i+1) + "| |")
    # prints the last line of the structure
    print(" "*2*(num-1) + "+-+")

downward_block(number)

