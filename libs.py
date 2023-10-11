################################################
#           Author: Mikael Larsson             #
#           Version: 1.0                       #
#           Modified date: 2023-10-09          #
################################################

import os
import random
import csv

def clear_screen():
    """
    Clear the terminal screen.

    This function clears the terminal or command prompt window 
    screen by issuing the appropriate command for the operating 
    system being used.

    Uses:
    - 'cls' command for Windows environments.
    - 'clear' command for Unix/Linux environments.
    """
    # Determine the OS type and select the appropriate clear screen command.
    # os.name == 'nt' indicates a Windows environment, while 'posix' indicates Unix/Linux.
    # os.system() is used to execute the chosen command.
    os.system('cls' if os.name == 'nt' else 'clear')



def random_line_csv(filename):
    """
    Retrieve a random word from a specified CSV file.
    
    Parameters:
    filename (str): The name/path of the CSV file.
    
    Returns:
    str: A randomly selected word from the file.
    
    Note:
    Ensure the CSV file exists and contains the necessary data. 
    Update the filename/path as per the requirement.
    """
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        words = [row[0] for row in reader]
        return random.choice(words)