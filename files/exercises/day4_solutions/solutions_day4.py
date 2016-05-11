## SJS 
## This file contains solutions for the Python exercises of Day 4



##################### Interacting with files ##################### 

## 1. Open the file "file1.txt" in read-mode, and print its contents to screen. For this, you should use the .read() method, which saves the contents of the file to a single string. Perform this task twice: once using open and close, and once using with control-flow.

# Using open and close
f = open("file1.txt", "r")
contents = f.read()
f.close()
print contents

# Using with
with open("file1.txt", "r") as f:
    contents = f.read()
print contents



## 2. Open the file "file1.txt" in read-mode, and save all lines in this file to a list using the .readlines() method. Write a new file called "upper_file1.txt" which contains the same contents of "file1.txt" but in upper-case. Try to do this task using a single for-loop.

with open("file1.txt", "r") as f:
    lines = f.readlines()

with open("upper_file1.txt", "w") as outfile:
    for line in lines:
        outfile.write(line.upper())




## 3. Open the file "upper_file1.txt" in read-mode, and append the sentence: "I just created this upper-case file!" to the bottom of the file.

with open("upper_file1.txt", "f") as f:
    f.write("\nI just created this upper-case file!")




## 4. Open the file "flu_sequences.fasta" in read-mode, and save the contents of a file as a single string using the .read() method (be sure to close the file, or use with control-flow!). Address the following questions using Python:

with open("flu_sequences.fasta", "r") as flufile:
    flu = flufile.read()

# (a) How many characters are in this file? Remember that .read() saves the entire file as a single string!
print len(flu)

# (b) How many lines are in this file? (Hint: use the .split() method as part of the solution).
no_endline = flu.strip("\n") # This method removes any extra newline characters at the end of the file
lines = no_endline.split("\n")
print len(lines)

# (c) Use a for-loop to print the first 10 lines of the file.
for i in range(10):
    print lines[i]
    
# (d) Open and read the file again, except this time, use the .readlines() method instead of .read(). Perform the same three tasks. (Hint: to count the characters, loop over the line list and keep a running counter of the length of each line.)
with open("flu_sequences.fasta", "r") as flufile:
    flulines = flufile.readlines()
    
# Number of characters
nchar = 0
for line in flulines:
    nchar += len(line)
print nchar

# Number of lines
print len(flulines)

# first 10 lines
for i in range(10):
    print flulines[i]







##################### Python modules ##################### 


## 1. For this question, you will use the os module. In the included zip directory, there are 20 text files named file1.txt, file2.txt, file3.txt,..., file20.txt (below, they are referred to as file<1-20.txt> for convenience). For this question, use python to count the number of lines in each file. You will save all file line-counts to a dictionary, in which the keys are the file names and the values are the line counts. Once you have created the dictionary, print it to screen to make sure it looks correct. Hint: Use the os module function os.listdir to list all files in the current directory and loop over all of these files in order to count their lines. To ensure that you are only counting lines in these text files, use the .startswith() and .endswith() method (all files start with "file" and all files end with ".txt").

import os
files = os.listdir("day4_files/") # remember to put the correct path here based on where you call this script from!
file_line_counts = {}
for file in files:
    if file.beginswith("file") and file.endswith(".txt"):
        
        with open(file, "r") as f:
            file_line_counts.append( len(f.readlines() )




##2. Create a new file called "file_full.txt" which contains all contents from each file<1-20>.txt (in order). Again, use os.listdir to loop over these files. Once this file has been created, use the shutil module to move the file to a different directory on your computer. After this script has run, navigate in your terminal (using the UNIX command cd) to this directory to confirm that "file_full.txt" is indeed there.

import os
import shutil

files = os.listdir("day4_files/") 

outfile = open("file_full.txt", "w")

for file in files:
    if file.beginswith("file") and file.endswith(".txt"):
        
        # Grab contents of file
        with open(file, "r") as f:
            contents = file.read()
        # Write those contents to full_file.txt
        outfile.write(contents + "\n")
outfile.close()

shutil.move("file_full.txt", "/Users/sjspielman/") # Moves the file to my home directory
        




## 3. Write a function which counts the number of times a given letter occurs in a file. The function should take two arguments: the file name (including its path) and the letter to count. The function should return the number of occurrences for that letter. Hnt: In this function, you should open the file, read it using the .read() method, and then use the .count() method to count the number of times the letter appears. Perform the following tasks with this function:

def count_letter_in_file(filename, letter):
    
    with open(filename, "r") as f:
        contents = f.read()
    
    letter_count = contents.count(letter)
    return letter_count
    
## (a)  Run this function on all file<1-20.txt> to count the letter "a". For every file which contains more than 100 a’s, use the shutil to make a copy of this file called "lots_fileX.txt". For example, if file10.txt contains more than 100 a’s, you should create a second file called "lots_file10.txt".

import shutil
threshold = 100
path = "day4_files/"
for i in range(1, 21):
    
    file = path + "file" + str(i) + ".txt"
    n = count_letter_in_file(file, "a")
    if n > threshold:
        newfile = path + "lots_file" + str(i) + ".txt"
        shutil.copy(file, newfile)
        

## (b) Use the sys module (specifically the sys.argv variable) to capture two command-line arguments: a file on which to run this function and the letter to count. Run the function using the given input parameters, and print a a sentence to the screen summarizing the results.

# Save this code to a file, let's say called "script1.py", and call as (for example):
#    python script1.py file1.txt b
import sys
file = sys.argv[1]
letter = sys.argv[2]
n = count_letter_in_file(file, letter)
print "In the file " + file + ", there are " + n + " occurrence(s) of the letter " + letter "."



## (c) Modify your code from the previous point to use the os module function os.path.exists(). This function takes a single argument, a path to a file/directory, and returns True or False indicating if the file exists or not. So, before running the function on the command-line provided file, check if the file exists using os.path.exists(). If the file exists, then proceed as usual. If the file does not exist, print to screen "Your file does not exist!", and then exit immediately with sys.exit().

# Again, save this code to a file and run
import sys
import os
file = sys.argv[1]
letter = sys.argv[2]

# Does the file exist?
if not os.path.exists(file):
    print "Your file does not exist!"
    sys.exit()
    
n = count_letter_in_file(file, letter)
print "In the file " + file + ", there are " + n + " occurrence(s) of the letter " + letter "."


## (d) Now, run the function from an entirely separate script. Accomplish this by importing the file with this function into the script you will run. You can run the function on a file of your choice.

# For this question, you should place the function definition in its own script, called function.py. Write this in a separate script:

import sys
# If the function.py is *not* in the same directory as this script, add the path with the next line (otherwise comment it out)
sys.path.append("directory/where/functions.py/is/located/")
import functions

file = "name_of_file.txt"
n = functions.count_letter_in_file(file, "d")


# For answer to the bonus question, see the script bonus.py






