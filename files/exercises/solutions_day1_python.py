## SJS 
## This file contains solutions for the Python exercises of Day 1


##################### Working with Lists ##################### 

## 1. Define a list variable called animals which contains the following six entries: "monkey", "giraffe", "shark", "caterpillar", "ctenophore", and "squid". Perform the following tasks on this variable:
animals = ["monkey", "giraffe", "shark", "caterpillar", "ctenophore", "squid"]

## (a) Use indexing to create a new list with just the items "monkey", "giraffe", and "shark".
short_animals = animals[:3]

## (b) Use negative indexing to extract "squid" from this list.
print animals[-1]

## (c) Use the list method .append() to add the animal "spider" to the end of the list. Use the len function to see the length of the animals list after appending.
animals.append("spider")
print len(animals) # The length is now 7, because append redefined the list in place

## (d) Use indexing to change the second entry in animals to "cat".
animals[1] = "cat"

## (e) Use the list method .pop() to remove the 3rd entry from this list.
animals.pop(2)

## (f) Create a second list called plants which contains the entries "tree", "flower", "bush", and "grass". Next, create another list called organisms, in which the first entry is the animals list and the second entry is the plants list, using this code: organisms = [plants, animals]. You have just created a "list of lists", or a nested list. Use the len() function to determine the length of this new list. Is this what you expected or not?
plants = ["tree", "flower", "bush", "grass"]
organisms = [plants, animals]
print len(organisms) # Prints 2, since this list contains two items. That these items are lists does not matter - organisms still has a length of 2.

## (g) Using indexing, replace the word "tree" in organisms with "redwood".
organisms[0][0] = "redwood"

## (h) Using indexing, extract the words "grass" and "caterpillar" from the organisms list in order to create this new list: ["grass", "caterpillar"]. Bonus - for this question, try to incorporate the .index() list method.
# Without index:
new_list = [ organisms[0][3], organisms[1][2] ]

# With index: 
grass_index = organisms[0].index("grass")
cater_index = organisms[1].index("caterpillar")
new_list = [ organisms[0][grass_index], organisms[1][cater_index] ]






##################### Working with Strings ##################### 

## 1. Define two string variables, one with the value "hello" and the other with the value "goodbye". Using concatenation (the + sign), create this new string: "helloGOODBYEHELLOgoodbye” from the two variables defined. Print your result to be sure it is correct.
a = "hello"
b = "goodbye"
c = a + b.upper() + a.upper() + b
print c

## 2. Create a string variable with the contents "abcdefg". From this variable, create a new string in which the "e" has been replaced with "X", i.e. "abcdXfg". Hint: use indexing and concatenation. Print a final statement that says: "My new string is abcdXfg."
letters = "abcdefg"
new_letters = letters[:4] + "X" + letters[5:]
print "My new string is " + new_letters 

## 3. Define a string variable with the following value: "Hi, my name is Joe. I got a wife and three kids. I work in a button factory." Perform the following tasks on this variable:
joe = "Hi, my name is Joe. I got a wife and three kids. I work in a button factory."

## (a) Extract the first 10 characters from the string.
joe1 = joe[:10]

## (b) Count of the number of occurrences of the letter "e" in the string.
num_e = joe.count("e")

## (c) Extract characters 8 - 14 from the string, and save this as a variable. Then, convert this new string to uppercase.
joe2 = joe[7:14].upper()

## (d) Convert this string into a list of lower-case words like this: ["hi", "my", "name", "is", "joe", "i", "got", "a", "wife", "and", "three", "kids", "i", "work", "in", "a", "button", "factory"].Forthistask,youwillneedtousethe.split() string method and indexing. Finally, use the len() function to determine how many words are in this new list.
lower_joe = joe.lower()
lower_joe2 = lower_joe.replace(".", "")
lower_joe2 = lower_joe.replace(",", "")
joe_as_list = lower_joe2.split(" ")









