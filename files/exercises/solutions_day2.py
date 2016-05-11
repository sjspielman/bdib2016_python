## SJS 
## This file contains solutions for the Python exercises of Day 2


##################### Working with Dictionaries ##################### 

## 1. Define this dictionary in Python: molecules = {"DNA":"nucleotides", "protein":"amino acids", "hair":"keratin"},and perform the following tasks:
molecules = {"DNA":"nucleotides", "protein":"amino acids", "hair":"keratin"}

## (a) Create two lists called molecules_keys and molecules_values, comprised of the keys and values in molecules, respectively. Use dictionary methods for this task.
molecules_keys = molecules.keys()
molecules_values = molecules.values()

## (b) Add the key:value pair "ribosomes":"RNA" to the molecules dictionary. Print the dictionary to confirm.
molecules["ribosomes"] = "RNA"
print molecules

## (c) Add yet another key:value pair, "ribosomes":"rRNA", to the molecules dictionary, and print out the new dictionary. Understand why the result contains the key:value pairs shown.
molecules["ribosomes"] = "rRNA" # the key:value pair "ribosomes":"RNA" is now gone and has been replaced!


## 2. Congratulations, you've been hired as a zoo-keeper! Now you have to feed the animals. You received these handy Python dictionaries which tells you (a) to which category each animal belongs, and (b) what to feed each animal category:
category = {"lion":  "carnivore", "gazelle":  "herbivore", "anteater": "insectivore", "alligator":  "homovore", "hedgehog":  "insectivore", "cow": "herbivore", "tiger":  "carnivore", "orangutan":  "frugivore"}

feed = {"carnivore":  "meat", "herbivore":  "grass", "frugivore":  "mangos", "homovore":  "visitors", "insectivore":  "termites"}

# Use indexing to determine what you should feed the orangutan and print the result.

print feed[category["orangutan"]]



##################### If/elif/else Exercises ##################### 

## 1. In Texas, you can be a member of the elite "top 1%" if you make at least $423,000 per year. Alternatively, in Hawaii, you can be a member once you start making at least $279,000 per year! Finally, if you live in New York, you need to earn at least $506,000 a year to make the cut. Andrew is CEO of Big Money Company, and he earns $425,000 per year, and Stacey is CEO of Gigantic Money Company with an annual salary of $700,000. Use if-statements to determine, and print, whether Andrew and Stacey would be considered top 1%-ers in Texas, Hawaii, and New York.

# Define 1% limits
texas = 423000
hawaii = 279000
newyork = 506000

# Define Andrew and Stacey salaries
andrew = 425000
stacey = 700000

# Evaluate Stacey across states, and do something similar for Andrew
if stacey >= texas:
    print "Stacey is a 1%er in Texas"
else:
    print "Stacey is not a 1%er in Texas"
if stacey >= hawaii:
    print "Stacey is a 1%er in Hawaii"
else:
    print "Stacey is not a 1%er in Hawaii"
if stacey >= newyork:
    print "Stacey is a 1%er in New York"
else:
    print "Stacey is not a 1%er in New York"    

# Alternatively, we can store 1% limits in a dictionary:
one_percent = {"texas":423000, "hawaii":279000, "newyork":506000}
if stacey >= one_percent["texas"]:
    print "Stacey is a 1%er in Texas"
else:
    print "Stacey is not a 1%er in Texas"
if stacey >= one_percent["hawaii"]:
    print "Stacey is a 1%er in Hawaii"
else:
    print "Stacey is not a 1%er in Hawaii"
if stacey >= one_percent["newyork"]:
    print "Stacey is a 1%er in New York"
else:
    print "Stacey is not a 1%er in New York"    
    
    
    

## 2. Copy and paste the list below into a Python script and perform the following tasks:
b = [19, 3, 2, 88, 82, 31, -9, 8, 33, -6, -111]

## (a) Write an if/else statement to determine whether the length of list b is greater than 10 (Hint: use the len function). If this condition is true, create a new list called newb that contains the first 5 numbers in b. If this condition is false, create a new list called newb that contains the last 5 numbers from list b.

if len(b) > 10:
    newb = b[5:]
else:
    newb = b[-5:]

## (b) Determine the sum of the list newb (Hint: use the sum() function, which returns the sum of a list, e.g. sum([1,2,3]) returns 6).

newb_sum = sum(newb)

## (c) Use an if/else statement to determine if this sum is even or odd (Hint: use the modulus operator, %), and print a sentence summarizing the result.

if newb_sum % 2 == 0:
    print "The sum is even."
else:
    print "The sum is odd."




##################### For-loop Exercises ##################### 

## 1. Write a for-loop to print the powers of 2, ranging from 2^0 to 2^15. (Note that in Python, the exponent symbol is **, as in 3**2 = 9).

for i in range(16):
    print 2**i


## 2. Modify your code from (1) such that all each power-of-2 value is saved to a list called powers2. Print the resulting list.

powers2 = []
for i in range(16):
    powers2.append( 2**i )

print powers2



## 3. This is the longest German word: "rindfleischetikettierungsuberwachungsaufgabenubertragungsgesetz" (accents removed), meaning "widow of a Danube steamboat company captain". Save this word to a string vari- able in Python, and count the number of times each letter in the alphabet (a-z) appears in this word. For every letter a-z, print the number of occurrences, e.g. "a: 4".

german_word = "rindfleischetikettierungsuberwachungsaufgabenubertragungsgesetz"
abc = "abcdefghijklmnopqrstuvwxyz"

for letter in abc:
    german_count = german_word.count(letter)
    print letter +  ": " + str(german_count)

## (a) Modify your code such that letters with a count of 0 do not get printed. Do this task twice, using two different strategies:

## Strategy 1: For each letter, decide after counting its occurrences if it should be printed or not

for letter in abc:
    german_count = german_word.count(letter)
    if german_count > 0:
        print letter +  ": " + str(german_count)
        
## Strategy 2: Use the in operator before determining each letter's count, and then only count the letter if it has a non-zero count.

for letter in abc:
    if letter in abc: 
        german_count = german_word.count(letter)
        print letter +  ": " + str(german_count)
        

## (b) Modify your code to save the total letter count (a single counter for all letters!) as you loop. For this, you will need to define a variable to store the sum, and you can increment this variable with counts as you go. Once this is complete, use an if-else statement to check that the total sum is equal to length of the full word. Print a statement indicating whether your sum is correct or not.

total_count = 0
for letter in abc:
    if letter in abc:
        german_count = german_word.count(letter)
        total_count += german_count
        print letter +  ": " + str(german_count)

if total_count == len(german_word):
    print "The total letter count is correct."
else:
    print "The total letter count is incorrect."
    
    
    
    
## 5. A silly professor has decided to curve grades in a very special way: grades above 95 are reduced by 10%, grades between 75-95 (inclusive) remain the same, and grades below 75 are raised by 10%. You have been tasked with crunching the numbers.    
    
## (a) Create a list of new grades that reflects these rules from the following grade list: grades = [45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58]    

grades = [45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58]    
new_grades = []

for grade in grades:
    if grade > 95:
        new_grades.append(grade * 0.9)
    elif grade <= 95 and grade >= 75:
        new_grades.append(grade)
    elif grade < 75: # Note that this could also be else, since no more conditions really exist besides this one.
        new_grades.append(grade * 1.1)         
    
## (b) The professor has changed his mind: he now wants to use a scaling factor of 0.078325 (instead of 0.1), because why not! Recompute the grades from part 1 using this new scaling. This time, round the grades to 2 decimal places using the function round(). 
    
grades = [45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58]    
new_grades = []

for grade in grades:
    if grade > 95:
        new = round(grade * (1. - 0.078325), 2)
        new_grades.append(new)
    elif grade <= 95 and grade >= 75:
        new_grades.append(grade)
    elif grade < 75: 
        new = round(grade * 1.078325, 2)
        new_grades.append(new)         


## (c) Finally, modify your code (if you need to) so that the scaling value (either 0.1 or 0.078325) used in your for-loop is a pre-defined variable to avoid hard-coding the scaling value.

scale = 0.078325
new_grades = []

for grade in grades:
    if grade > 95:
        new = round(grade * (1. - scale), 2)
        new_grades.append(new)
    elif grade <= 95 and grade >= 75:
        new_grades.append(grade)
    elif grade < 75: 
        new = round(grade * (1. + scale), 2)
        new_grades.append(new)         
   
    
## (d) The nested list below contains three sets of grades for silly professor's three class sections: all_grades = [[45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58], [23, 46, 17, 67, 55, 42, 31, 73], [91, 83, 79, 76, 82, 91, 95, 77, 82, 77]]. Create a new nested list with the curved grades for each of these groups, using a scaling factor of 0.06.   

all_grades = [[45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58], [23, 46, 17, 67, 55, 42, 31, 73], [91, 83, 79, 76, 82, 91, 95, 77, 82, 77]]    
new_grades = []
scale = 0.06

for group in all_grades:
    
    new_group = []
    for grade in group:
        if grade > 95:
            new = round(grade * (1. - scale), 2)
            new_group.append(new)
        elif grade <= 95 and grade >= 75:
            new_group.append(grade)
        elif grade < 75: 
            new = round(grade * (1. + scale), 2)
            new_group.append(new)   
                   
    new_grades.append(new_group)



## 5. Using the zoo-keeper dictionaries from today's second dictionary exercise, loop over the animals in each category and, using the feed dictionary, determine and print what food each animal should eat, e.g. "The gazelle should eat grass."
category = {"lion":  "carnivore", "gazelle":  "herbivore", "anteater": "insectivore", "alligator":  "homovore", "hedgehog":  "insectivore", "cow": "herbivore", "tiger":  "carnivore", "orangutan":  "frugivore"}

feed = {"carnivore":  "meat", "herbivore":  "grass", "frugivore":  "mangos", "homovore":  "visitors", "insectivore":  "termites"}
 
for animal in category:
    print "The " + animal + " should eat " + feed[category[animal]]
    
     

## 6. This dictionary provides the molecular weight for all amino acids: amino_weights = {"A":89.09, "R":174.20, "N":132.12, "D":133.10, "C":121.15, "Q":146.15, "E":147.13, "G":75.07, "H":155.16, "I":131.17, "L":131.17, "K":146.19, "M":149.21, "F":165.19, "P":115.13 "S":105.09, "T":119.12, "W":204.23, "Y":181.19, "V":117.15}. Perform the following tasks with this dictionary.
amino_weights = {"A":89.09, "R":174.20, "N":132.12, "D":133.10, "C":121.15, "Q":146.15, "E":147.13, "G":75.07, "H":155.16, "I":131.17, "L":131.17, "K":146.19, "M":149.21, "F":165.19, "P":115.13, "S":105.09, "T":119.12, "W":204.23, "Y":181.19, "V":117.15}

## (a) Determine the molecular weight for this protein sequence: "GAHYADPLVKMPWRTHC".

protein = "GAHYADPLVKMPWRTHC"
weight = 0.
for amino_acid in protein:
    weight += amino_weights[amino_acid]
    
## (b) This protein sequence, "KLSJXXFOWXNNCPR" contains some ambiguous amino acids, coded by "X". Calculate the molecular weight for this protein sequence. To compute a weight for an ambiguous amino acid "X", use the average amino acid weight.    

mean_weight = sum(amino_weights.values()) / len(amino_weights)

protein = "KLSJXXFOWXNNCPR" 
weight = 0.
for amino_acid in protein:
    if amino_acid in amino_weights:
        weight += amino_weights[amino_acid]
    else:
        weight += mean_weight

# Alternatively, we can add mean_weight into the dictionary
amino_weights["ambig"] = mean_weight
weight = 0.
for amino_acid in protein:
    if amino_acid in amino_weights:
        weight += amino_weights[amino_acid]
    else:
        weight += amino_weights["ambig"]


## 7. Using the method .startswith(), determine if the sentence "Dan's dog, dubbed Fluffy, dove deep in the dam and drank dirty water, but he didn't drown" is an alliteration for the letter "d". For the purposes of this example, let's assume that if at least 50% of the words start with the same letter, then it is alliteration. Otherwise, it is not.

sentence = "Dan's dog, dubbed Fluffy, dove deep in the dam and drank dirty water, but he didn't drown"
sentence_list = sentence.split(" ")

total_d = 0.
for word in sentence_list:
    # Check upper and lower case!
    if word.startswith("d") or word.startswith("D"):
        total_d += 1.

# If/else to determine alliteration
frac_d = total_d / len(sentence_list)
if frac_d >= 0.5:
    print "Yes, this is alliteration"
else:
    print "No, this is not alliteration"

# Note that another strategy would be to convert the sentence to entirely upper/lower case before any processing, so that we don't have to check for both capital and lower letters

sentence = "Dan's dog, dubbed Fluffy, dove deep in the dam and drank dirty water, but he didn't drown"
sentence_list = sentence.upper().split(" ")

total_d = 0.
for word in sentence_list:
    if word.startswith("D"):
        total_d += 1.

# If/else to determine alliteration
frac_d = total_d / len(sentence_list)
if frac_d >= 0.5:
    print "Yes, this is alliteration"
else:
    print "No, this is not alliteration"
 
    
    
    
    
    
    
    
    
    
    
    
    
