## SJS 
## This file contains functions, the solutions for the Python exercises of Day 3


# Function to print if a given salary is a top-1% salary in Texas, Hawaii, and New York
def top_one_percent(salary):
    

    # Define 1% limits
    texas = 423000
    hawaii = 279000
    newyork = 506000
    
    # evaluate across states
    if salary >= texas:
        print "This salary is a 1%er in Texas"
    else:
        print "This salary is not a 1%er in Texas"
    if salary >= hawaii:
        print "This salary is a 1%er in Hawaii"
    else:
        print "This salary is not a 1%er in Hawaii"
    if salary >= newyork:
        print "This salary is a 1%er in New York"
    else:
        print "This salary is not a 1%er in New York"    
        

# Function to build a list of exponents 0-15 for a given number
def compute_powers(x)

    p = []
    for i in range(16):
        p.append(x**i)
    
    return p
    
    
# Function to curve grades according to silly professor    
def curve_grades(grade_list, above_cutoff, below_butoff, scale):
    
    new_grades = []
    
    for grade in grade_list:
        if grade > above_cutoff:
            new_grades.append(grade * (1. - scale) )
        
        elif grade <= above_cutoff and grade >= below_cutoff:
            new_grades.append(grade)
        
        elif grade < below_cutoff:
            new_grades.append(grade * (1. + scale) )
    
    return new_grades
    

# Function to compute the molecular weight of a given protein sequence 
def compute_molecular_weight(protein):
    
    amino_weights = {"A":89.09, "R":174.20, "N":132.12, "D":133.10, "C":121.15,"Q":146.15, "E":147.13, "G":75.07, "H":155.16, "I":131.17, "L":131.17,"K":146.19, "M":149.21, "F":165.19, "P":115.13, "S":105.09, "T":119.12, "W":204.23, "Y":181.19, "V":117.15}
    
    # Compute weight for an ambiguous/unknown character as the mean amino acid weight
    ambig_weight = sum(amino_weights.values()) / len(amino_weights)
    
    weight = 0.
    for aa in protein:
        if aa in amino_weights:
            weight += amino_weights[aa]
        else:
            weight += ambig_weight
    
    return weight
        
    

# Function to determine if given string is alliteration for a provided letter. The argument cutoff is the percentage of words which must start with the given letter for it to be alliteration.
def is_it_alliteration(sentence, letter, cutoff):
    
    # Turn sentence into list of lower-case letters for parsing, and make letter lower in case!
    sentence = sentence.lower()
    as_list = sentence.split(" ")
    letter = letter.lower()
    
    total_allit = 0.
    for entry in as_list:
        if entry.beginswith(letter):
            total_allit += 1
    
    if total_allit / len(as_list) >= cutoff:
        return True
    else:
        return False
        
        
    
    
    
    
        
