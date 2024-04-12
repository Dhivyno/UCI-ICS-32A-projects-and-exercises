import os
import os.path

# function for error handling and going back to the start after error
def error():
    print("ERROR")
    start()

# function for listing everything in source directory
def list_only(path):
    subdir_list = []
    # saves the list of files and directories in the input "path" to "result"
    result = os.listdir(path)
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in result:
        if os.path.isfile(os.path.join(path, content)):
            print(os.path.join(path, content))
        elif os.path.isdir(os.path.join(path, content)):
            subdir_list.append(os.path.join(path, content))
    for subdir in subdir_list:
        print(subdir)
        
# function for listing all subdirectories and files in source directory and all subdirectories
def list_recursion(path):
    subdir_list = []
    # saves the list of files and directories in the input "path" to "result"
    result = os.listdir(path)
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in result:
        if os.path.isfile(os.path.join(path, content)):
            print(os.path.join(path, content))
        # if path of item is a directory, adds to a list of subdirectories "subdir_list"
        elif os.path.isdir(os.path.join(path, content)):
            subdir_list.append(os.path.join(path, content))
    for subdir in subdir_list:
        # applies the list_recursion function to each subdirectory
        print(subdir)
        list_recursion(subdir)

# function for listing only the files in the source directory and no subdirectories
def list_files_only(path):
    subdir_list = []
    # saves the list of files and directories in the input "path" to "result"
    result = os.listdir(path)
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in result:
        if os.path.isfile(os.path.join(path, content)):
            print(os.path.join(path, content))

# function for listing only the files in the source directory and all subdirectories
def list_recursion_files_only(path):
    subdir_list = []
    # saves the list of files and directories in the input "path" to "result"
    result = os.listdir(path)
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in result:
        if os.path.isfile(os.path.join(path, content)):
            print(os.path.join(path, content))
        elif os.path.isdir(os.path.join(path, content)):
            subdir_list.append(os.path.join(path, content))
    for subdir in subdir_list:
        list_recursion_files_only(subdir)

# function for searching a specific file name within the source directory and all subdirectories
def recursion_search(path, file_name):
    subdir_list = []
    # saves the list of files and directories in the input "path" to "result"
    result = os.listdir(path)
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in result:
        if os.path.isfile(os.path.join(path, content)) and content == file_name:
            print(os.path.join(path, content))
        elif os.path.isdir(os.path.join(path, content)):
            subdir_list.append(os.path.join(path, content))
    for subdir in subdir_list:
        recursion_search(subdir, file_name)

def search(path, file_name):
    subdir_list = []
    # saves the list of files and directories in the input "path" to "result"
    result = os.listdir(path)
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in result:
        if os.path.isfile(os.path.join(path, content)) and content == file_name:
            print(os.path.join(path, content))
    
def recursion_extension_search(path, extension):
    subdir_list = []
    # saves the list of files and directories in the input "path" to "result"
    result = os.listdir(path)
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in result:
        if os.path.isfile(os.path.join(path, content)) and content.endswith("."+extension):
            print(os.path.join(path, content))
        elif os.path.isdir(os.path.join(path, content)):
            subdir_list.append(os.path.join(path, content))
    for subdir in subdir_list:
        recursion_extension_search(subdir, extension)

def extension_search(path, extension):
    subdir_list = []
    # saves the list of files and directories in the input "path" to "result"
    result = os.listdir(path)
    # checks if path of each item in the source directory is file and prints the path if it is a file
    for content in result:
        if os.path.isfile(os.path.join(path, content)) and content.endswith("."+extension):
            print(os.path.join(path, content))

def create_file(path, file_name):
    # Create the folder if it doesn't already exist 
    if not os.path.exists(path): 
        os.mkdir(path) 
    
    # Create the file inside the given folder 
    with open(os.path.join(path,(file_name+".dsu")), 'w') as f: 
        pass
        # applies search function to find and print the path of the created file
    search(path, file_name+".dsu")
    
# function to delete a file given its path
def delete_file(path_to_file):
    os.remove(path_to_file)
    print(path_to_file+" DELETED")


def print_contents_of_file(path_to_file):
    # if file is not a .dsu file then error is raised
    if not path_to_file.endswith(".dsu"):
        error()
    else:
        # opens the file and prints each line iteratively
        with open(path_to_file, "r") as f:
            for line in f:
                print(line.strip("\n"))


# clever function to overcome unexpected whitespaces in the input
def find_path_from_cmd_list(cmd_list):
    # sets the index of the first option to be the end of the command given in case there is no option with "-" given
    first_option_index = len(cmd_list)
    # finds the first index where there is an occurence of "-" to find where the first option command is
    for i in range(len(cmd_list)):
        if "-" == cmd_list[i][0]:
            first_option_index = i
            break
    # makes the path variable by concatenating everything between the first command (L, Q, C, D, R) and the first option
    path = ""
    for i in range(1, first_option_index):
        if i != first_option_index-1:
            path += cmd_list[i] + " "
        else:
            path += cmd_list[i]
    return(path)

def exec(cmd_list, recursion_option: bool, files_only_option: bool, search_option: bool, extension_search_option: bool, file_name_for_creation_given: bool):
    # sets the path variable as the concatenation of all elements from the second to the first option index in the input command 
    path = find_path_from_cmd_list(cmd_list)

    if cmd_list[-1][0] != "-":
        extra_input = cmd_list[-1]

    # checks for each combination of commands and options
    if "L" in cmd_list and recursion_option and files_only_option:
        try:
            list_recursion_files_only(path)
        except:
            error()
    elif "L" in cmd_list and recursion_option and extension_search_option:
        try:
            recursion_extension_search(path, extra_input)
        except:
            error()
    elif "L" in cmd_list and search_option and recursion_option:
        try:
            recursion_search(path, extra_input)
        except:
            error()
    elif "L" in cmd_list and extension_search_option:
        try:
            extension_search(path, extra_input)
        except:
            error()
    elif "L" in cmd_list and search_option:
        try:
            search(path, extra_input)
        except:
            error()
    elif "L" in cmd_list and files_only_option:
        try:
            list_files_only(path)
        except:
            error()
    elif "L" in cmd_list and recursion_option:
        try:
            list_recursion(path)
        except:
            error()
    elif "L" in cmd_list:
        try:
            list_only(path)
        except:
            error()
    elif "C" in cmd_list and file_name_for_creation_given:
        try:
            create_file(path, extra_input)
        except:
            error()
    elif "D" in cmd_list:
        try:
            delete_file(path)
        except:
            error()
    elif "R" in cmd_list:
        try:
            print_contents_of_file(path)
        except:
            error()


def preprocessing(cmd_list):
    # sets boolean variable for every possible option (r, f, s, e) and the file name for C command
    recursion_option = False
    files_only_option = False
    search_option = False
    extension_search_option = False
    file_name_for_creation_given = False
    option_list = []
    # adds each occurence of an option to a list "option_list"
    for element in cmd_list:
        if "-" in element and len(element) == 2:
            option_list.append(element[1])
    # checks each option in "option_list" and toggles the respective boolean variable
    if "r" in option_list:
        recursion_option = True
    if "f" in option_list:
        files_only_option = True
    if "s" in option_list:
        search_option = True
    if "e" in option_list:
        extension_search_option = True
    if "n" in option_list:
        file_name_for_creation_given = True
    # executes the next phase of processing "exec"
    try:
        exec(cmd_list, recursion_option, files_only_option, search_option, extension_search_option, file_name_for_creation_given)
    except:
        error()
    
def start():
    cmd = ""
    while cmd != "Q":
        # collects input from user
        cmd = input()
        # splits the full command into the subsections
        try:
            cmd_list = cmd.split(" ")
            path = os.path.normpath(find_path_from_cmd_list(cmd_list))
        except:
            error()
        # check if path given is a valid path and ask for another input if not
        while cmd != "Q" and (len(cmd_list) <= 1 or (cmd_list[0] != "C" and not os.path.isdir(path) and not os.path.isfile(path))):
            error()
            cmd = input()
            cmd_list = cmd.split(" ")
        try:
            preprocessing(cmd_list)
        except:
            error()

# to make sure the program is only started when the module is run rather than when imported
if __name__ == "__main__":
    start()        
