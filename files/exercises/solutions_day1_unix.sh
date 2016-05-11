## SJS 
## This file contains solutions for the Unix exercises of Day 1

##################### Question 2 ##################### 
## (a) Use the command mkdir to create a new directory called "blob".
mkdir blob

## (b) Use the command touch to create a new file called "blerg.txt".
touch blerg.txt

## (c) Use the command echo along with the symbol > to add the sentence "I’m writing to a file!" to blerg.txt.
echo "I'm writing to a file!" > blerg.txt

## (d) Use the command mv to move this file into the directory blob. Then, enter ls. What do you notice?
mv blerg.txt blob/
ls # Reveals that there is no longer a blerg.txt file in the current directory

## (e) Navigate into the directory "blob". Make a copy of blerg.txt called "blerg2.txt".
cd blob
cp blerg.txt blerg2.txt

## (f) Use the command echo and the symbol > to write the line "Another sentence!" to blerg2.txt. Now use less to examine the contents of blerg2.txt. What do you notice?
echo "Another sentence!" > blerg2.txt
less blerg2.txt # Reveals that the previous contents, "I'm writing to a file!", were overwritten. The file only contains the words "Another sentence!"

## (g) Make a new copy of the file blerg.txt using the command cp, called blerg3.txt. Enter ls. What files now exist in this directory?
cp blerg.txt blerg3.txt
ls # There are now three blerg files: blerg.txt, blerg2.txt, blerg3.txt . Copying files does not remove the original

## (h) Append the line "Another sentence!" to blerg3.txt using echo and the symbol >>.
echo "Another sentence!" >> blerg3.txt

## (i) Navigate back to your home directory (try using the code cd .. for this), and use the command rm -r to delete the blob directory.
cd ..
rm -r blob

## (j) Use the rm command to delete the file blerg.txt.
rm blerg.txt


##################### Question 3 ##################### 
## (a) The UNIX command wc stands for "word count". This command counts the number of lines, words, and bytes in a given file. Enter the command wc flu_sequences.fasta to display this information. Compare the result with the file size as displayed by ls -l. Do you see any overlapping numbers?
wc flu_sequences.fasta
ls -lh # reveals that the file byte size is the same 

## (b) Use wc with the argument -l to determine just the number of lines in sequences.fasta.
wc -l flu_sequences.fasta

## (c) Enter the command head flu_sequences.fasta to view the top few 10 lines of this file. Consult the documentation for head using the command man head, and figure out how to specify a different number of lines. Enter q to exit from the man documentation, and use your new knowledge to display the first 16 lines of the file.
head flu_sequences.fasta
man head
head -n 16 flu_sequences.fasta

## (d) Create a new file called "lastseqs.fasta" which contains the last 8 lines of flu_sequences.fasta (hint: the command tail, which is basically the opposite of head should be useful!). For this task, do not use touch.
tail -n 8 flu_sequences.fasta > lastseqs.fasta