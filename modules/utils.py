from os import listdir

def get_file_names(folderpath,out="output.txt"):
    list = listdir(folderpath)
    with open(out, 'w') as o:
        for l in list:
            o.write(l + " ")
        print(listdir(folderpath))
           # o.write(listdir(folderpath))
    print('File is ready: ', out)
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""

def get_all_file_names(folderpath,out="output.txt"):
    pass
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

def print_line_one(file_names):
    pass
    """takes a list of filenames and print the first line of each"""

def print_emails(file_names):
    pass
    """takes a list of filenames and print each line that contains an email (just look for @)"""

def write_headlines(md_files, out="output.txt"):
    pass
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""