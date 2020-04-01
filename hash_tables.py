# --------------------------------------- INSTRUCTIONS ---------------------------------------
# For this Assignment you will write your own HashTable in Python or Java. Do not use any built in Hashing Structures (dictionaries, Maps,Etc). For Simplicity sake make the underlying structure a basic array or list.

# You will :

# Read in the file below
# https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa.txt
# Store each word in your HashTable for easy lookup
# You will have to build a hash() function to give an integer value for your String
# Store the String in that index
# If a Collision, use a collision mitigation strategy
# Calculate and report the percentage of collisions in your structure
# Your HashTable may not be more than 20% larger than the # of total words

# ---------------------------------------- CODE -----------------------------------------------
import math

# This gives us a unique number (hash) per string
def get_hash(string):
    ascii_codes = {
        "a":97,
        "b":98,
        "c":99,
        "d":100,
        "e":101,
        "f":102,
        "g":103,
        "h":104,
        "i":105,
        "j":106,
        "k":107,
        "l":108,
        "m":109,
        "n":110,
        "o":111,
        "p":112,
        "q":113,
        "r":114,
        "s":115,
        "t":116,
        "u":117,
        "v":118,
        "w":119,
        "x":120,
        "y":121,
        "z":122   
    }

    word_length = len(string)
    letter_codes = []
    word_code  = 0
    

    # Each letter gets a unique code
    for i,item in enumerate(string):
        ascii_code = ord(string[i])
        ascii_next = 0
        ascii_next2 = 0
        if i == len(string)-1:     # If we're at the position of the last letter
            ascii_next = 100
        else:                      # If we're not at our last letter, we get the ascii of the next letter
            ascii_next = ord(string[i+1])
            if i == len(string)-2:
                ascii_next2 = 117 # A random number to spice things up :)
            else:
                ascii_next2 = ord(string[i+2])
        letter_code1 = math.log(ascii_next*word_length/ascii_code)
        letter_code2 = ascii_next2 #/ (word_length + math.log(ascii_code))
        letter_code = (letter_code1 * letter_code2)
        letter_codes.append(letter_code)
        # print("Letter code1 is {}".format(letter_code1))
        # print("Letter code2 is {}".format(letter_code2))
        # print("Letter code is {}".format(letter_code))
        
    # All the letter codes are added to get a unique number for the word
    for code in letter_codes:
        word_code += code
 
    # Ultimately I want to improve this because rn I'm using the word_code as the hash index. Ideally the word code would be used to create a smaller hash index: maybe using modulo?
    hash_index = word_code
    return hash_index

def cleanUp(word_list):
    for i,word in enumerate(word_list):
        try:
            if word.index("\n"):
                word_list[i] = word[:word.index("\n")]
        except ValueError:
            word = word
    return(word_list)
    

def run_hashing():
    with open("google-10000-english-usa.txt","r") as file:
        content = file.readlines() # A list of 10000 words
        content = cleanUp(content)
        
        # Creating our hash_table
        my_hash_table = []
        for i in content:
            my_hash_table.append("")
        collisions = 0

        # We create a hash table the size of our data (maybe it should be greater??)
        for index,item in enumerate(content):
            # We get a hash index for each word and insert it at that position of the list
            hash_index = int(get_hash(item))
            # with open ("help.txt","w") as helpfile:
            #     helpfile.writelines("{}".format(content))
            try:
                if my_hash_table[hash_index] != "":  # If there is already something at the location I want to add our new word to -> it means there's a collision
                    collisions += 1
                    with open("collisions.txt","a") as write: # Logging them to a file so we can analyze everything later
                        currentword = item
                        other = my_hash_table[hash_index]
                        other_hash = get_hash(other)
                        write.writelines("Current index is {}. CWord is {} and other is {} and oIs{}".format(hash_index,currentword,other,other_hash))
                    my_hash_table[len(my_hash_table)-hash_index] = item # Our collision mititgation strategy is placing the item from the end of the hash table 
                else:
                    my_hash_table[hash_index] = item  # By 'int-ing' our returned value from our hash table we're actually affecting it somehow. Can work more on this later.

            except IndexError:
                collisions += 0 

        print(my_hash_table)
        print("Percentage of collisions: {}%".format((collisions/len(content))*100))

#run_hashing()


run_hashing()
print(int(get_hash("item")))
print(int(get_hash("mail")))


# So the code was actually registering the \n as part of the string!!!!



    
# We have two things we dealing with: list index out of range, and then the actual collisions.

    
# Our helper functions (native python)
# print(ord("h")) #Gives us the ascii code of a character
# print(chr(107)) #Gives us the character behind an ascii code
# print(math.log(4,5)) 

    