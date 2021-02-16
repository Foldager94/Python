import os
import re

def get_file_names(folderpath,out="output.txt"):
    list = listdir(folderpath)
    with open(out, 'w') as o:
        for l in list:
            o.write(l + " ")
        print(listdir(folderpath))
    print('File is ready: ', out)
    
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""

def get_all_file_names(folderpath,out="output.txt"):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            with open(out, "a") as o:
                    o.write(file + "\n")
    
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

def print_line_one(file_names):
    for file in file_names:
        with open(file, "r") as o:
            print(o.readline())
            
    """takes a list of filenames and print the first line of each"""

def print_emails(file_names):
    for file in file_names:
        with open(file, 'r') as f:
            for line in f:
                if re.search(r'[\w\.-]+@[\w\.-]+', line):
                    print(line)
                
    """takes a list of filenames and print each line that contains an email (just look for @)"""

def write_headlines(md_files, out="output.txt"):
    for file in md_files:
        with open(file, 'r') as f:
            for line in f:
                if re.search("^#", line):
                    with open(out, 'a') as o:
                        o.write(line + "\n")

    """takes a list of md files and writes all headlines (lines starting with #) to a file"""