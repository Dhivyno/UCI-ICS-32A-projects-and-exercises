def partial_print(string: str):
    result = ""
    for i in range(0, len(string), 2):
        result += "^"+string[i]+"^"
    result += "\n"
    print(result)


if __name__ == "__main__":
    partial_print("0123456789")
    
    partial_print("BooIsHappyToday!")