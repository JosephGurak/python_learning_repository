# Dictionary for methods and other things to know

# have user be able to have keys displayed
# have a key be searchable ie if they type .copy() then it will pull the value for that key if it's in the library
# have user be able to then choose a key to show its value
# let user keep inputting requests



library = {      ###Continue adding examples to the keys and add more to the dictionary ###
    "set": {  # This is all the set methods
        ".add()": "Adds an element to the set",
        ".clear()": "Removes all elements from the set",
        ".copy()": "This will copy the entire list to a new variable",
        ".difference()": "Returns a set containing the difference between two or more sets",
        ".difference_update()": "Removes the Items in this set that are also included in another defined set",
        ".discard()": "Remove the specified item from the set",
        ".intersection()": "Returns a set that is the intersection of two or more sets",
        ".intersection_update()": "Removes the items in this set that are not present in the other specified set(s)",
        ".isdisjoint()": "Returns whether the two sets have an intersection",
        ".issubset()": "Returns whether another set contains this set",
        ".issuperset()": "Returns whether this set contains another set",
        ".pop()": "Removes an element from the end of the set",
        ".remove()": "Removes the specified element",
        ".symmetric_difference()": "Returns a set with the symmetric differences of the two sets",
        ".symmetric_difference_update()": "Inserts the symmetric differences form this set and another",
        ".union()": "Return a set containing the union of sets",
        ".update()": "Updates the set with another set or any other iterable"
    },
    "list": {  # This is all the list methods
        ".append()": "Adds an element at the end of the list",
        ".clear()": "Removes all the elements from the list",
        ".copy()": "This will copy the entire list to a new variable",
        ".count()": "Returns the number of elements with the specified value",
        ".extend()": "Add the elements of a list or any iterable to the end of the current list",
        ".index()": "Returns the index of the first element with the specified value",
        ".insert()": "Adds an element at the specified position",
        ".pop()": ["Removes the element at the specified position",
                   "Example: my_list.pop"],
        ".remove()": "Removes the first element with the specified value ",
        ".reverse()": "Reverses the order of the list",
        ".sort()": "Sorts the list"
    },
    "dict": {  # This is all the dict methods
        ".clear()": "Removes all the elements from the dictionary",
        ".copy()": "This will copy the entire list to a new variable",
        ".fromkeys()": "Returns a dictionary with the specified keys and values",
        ".get()": "Returns the value of the specified key",
        ".items()": "Returns a list containing the tuple for each key value pair",
        ".keys()": "Returns a list containing the dictionaries keys",
        ".pop()": "Removes the element with the specified key",
        ".popitem()": "Removes the last inserted key-value pair from the dictionary",
        ".setdefault()": "Returns the value of the specified key. If the key does not exist: insert the key with the specified value",
        ".update()": "Updates the dictionary with the specified key-value pairs",
        ".values()": "Returns a list of all the values in the dictionary",
    },
    "string": {  # This is all the string methods
        ".capitalize()": "Converts the first character to uppercase",
        ".lower()": "Converts string to lowercase",
        ".upper()": "Converts string to uppercase",
        ".center()": "Returns a centered String",
        ".count()": "Returns the number of occurrences of the value in a string",
        ".encode()": "Returns an encoded version of the string",
        ".endswith()": "Returns true if the string ends with the specified value",
        ".exapndtabs()": "Sets the Tab size of the string",
        ".find()": "Returns the index of the FIRST occurrence of the the specified value",
        ".format()": "Formats the specified values in a string",
        ".format_map()": "Formats the specified values in a string",
        ".index()": "Searches the string for the specified value and returns its position",
        ".isalnum()": "Returns true if all the characters in the string are alphanumeric",
        ".isalpha()": "Returns true if all the characters in the string are in the alphabet",
        ".isascii()": "Returns true if all the characters in the string are ascii characters",
        ".isdecimal()": "Returns true if all the characters in the string are decimals",
        ".isdigit()": "Returns true if all the characters in the string are digits",
        ".isidentifier()": "Returns true if the string is an identifier",
        ".islower()": "Returns true if all the character in the string are lower case",
        ".isupper()": "Returns true if all the characters in the string are upper case",
        ".isnumeric()": "Returns true if all the characters in the string are numeric",
        ".isprintable()": "Returns true if all the characters in the string are printable",
        ".isspace()": "Returns true if all the characters in the string are whitespace",
        ".istitle()": "Returns true if the string follows the rules of a title",
        ".join()": "Converts the elements of an iterable into a string",
        ".ljust()": "Returns a left justified version of the string",
        ".lstrip()": "Returns a left trim version of the string",
        ".maketrans()": "Returns a translation table to be used in translations",
        ".replace()": "Returns a string where the specified value is replaced with a specified value",
        ".partition()": "Searches for the specified string, and splits the string into a tuple containing three elements; The first element contains the part before the specified string, The second element contains the specified string, The third element contains the part after the string",
        ".rpartition()": "Searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements; The first element contains the part before the specified string, The second element contains the specified string, The third element contains the part after the string",
        ".rfind()": "Searches the string for a specified value and returns the last position of where it was found",
        ".rindex()": "Searches for the string for a specified value and returns the last position of where it was found",
        ".rjust()": "Returns a right justified version of the string",
        ".rsplit()": "Splits the string at the specified separator starting from the right and returns a list",
        ".rstrip()": "Returns a right trim version of the string",
        ".split()": "Splits the string at the specified separator and returns a list",
        ".splitlines()": "Splits the string at the line breaks and returns a list",
        ".startswith()": "Returns true if the string starts with the specified value",
        ".strip()": "Returns a trimmed version of the string",
        ".swapcase()": "Swaps cases of the string: uppercase --> lowercase , lowercase --> uppercase",
        ".title()": "Converts the character of each word to upper case in the string",
        ".translate()": "Returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table",
        ".zfill()": "Fills the string with a specified number of zeroes at the beginning of the string to make the string a certain desired length"
    },
    "Keywords": {
        "and": "A logical operator used to combine conditional statements",
        "as": "Used to create an alias",
        "assert": None,
        "break": "To break out of a loop",
        "class": "To define a class",
        "continue": "To continue to the next iteration of a loop",
        "def": "Defines a function"
    }
}


print('\n\t\033[4;34m Python Repository for the Over Caffeinated Grinders \033[0;0m\n')

# redo the menu and options into a function
#add the flashcard game for memorization
def main_menu():
    print("0) Search for Method")
    print("1) Display Library")
    print("2) Exit")

while True:
    main_menu()
    choice = input("Choose option Number:")
    if choice == '0':
        try:
            print("\033[4;34m Current Data Types in Library are: \033[0;0m\n")
            for keys in library:
                print(f"{keys} ", end='')
            my_query = input("\nWhich of the following Categories are you looking for?: ")
            print(f"These are the following methods for {my_query}:")
            for keys in library[my_query]:
                print(f"{keys} ", end='')
            print("\n\033[4;34m You need to input the method as follows:\033[0;0m .method() \n")
            key_value = input("Which Method are you looking for?: ")
            for value in library[my_query][key_value]:
                print("\t", value)
        except:
            print("\tThese are not the Methods you are looking for\n\n")
    if choice == '1':
        try:
            print(library.keys())
        except:
            print('Utter Failure')
    if choice == '2':
        print("\tWe'll Cover this later but for now...\n\n")
        break