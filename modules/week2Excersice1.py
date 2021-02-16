import argparse
import csv

def print_file_content(file_path):
    with open(file_path) as file_object:
        contents = file_object.read()
        print(contents)
    
def write_list_to_file_A(output_file, lst):
    with open(output_file, "w") as o:
        o.write(" ".join(lst) + "\n")
        
def write_list_to_file_B(output_file, *str):
    with open(output_file, "w") as o:
        for s in str:
            o.write(s + "\n")
            
def write_list_to_file_C(output_file, lst):
    with open(output_file, "w") as file:
        for l in lst:
            file.write(l + "\n")
    
def read_csv(input_file):
    with open(input_file, newline='') as o:
        reader = csv.reader(o)
        theList = list(reader)
    print(theList)





if __name__ == "__main__":
    """run with python w2.py input.txt -f output.txt -l word1 word2 word3"""
    parser = argparse.ArgumentParser(description='Solution to handin week 2')
    parser.add_argument('input_file', help='the input file to consume')
    parser.add_argument('-l', '--list', nargs='*', help='extra words', required=False)
    parser.add_argument('-f', '--output_file', help='the file to print to. (console if nothing is given)')
    args = parser.parse_args()
    inputfile = args.input_file
    outputfile = args.output_file
    argslist = args.list
    

    # only first arg
    if (outputfile and argslist):
        write_list_to_file_C(outputfile, argslist)
    # only input and output
    if (argslist):
        if not (outputfile):
            print(argslist)
    else:
        print_file_content(inputfile)
        
        
        