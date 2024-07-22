file_path = "books/frankenstein.txt"
def main():
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

contents = main() # pass main() to variable
def count(contents):    #define function which uses main
    count = 0
    words = contents.split() #split contents into list
    for word in words:
        count += 1
    return count

def count_characters(contents):
    characters_dict = {}
    lowered_contents = contents.lower() #convert characters to lowercase
    for character in lowered_contents:
        if character.isalpha(): # ensure only alphabetic characters
            if character in characters_dict:
                characters_dict[character] += 1
            else:
                characters_dict[character] = 1
    return characters_dict

# Begin Report Section ------------------------------

# Print Report Introduction
print(f"--- Begin report of {file_path} ---")

# Get the word count
word_count = count(contents)
print(f'{word_count} words found in the document')

# Get character count dictionary
characters_dict = count_characters(contents)

# Convert character count dictionary into list of dictionaries
# Note this is a list comprehension 
list_of_dicts = [{"character": key, "num": value} for key, value in characters_dict.items()]

# Takes dict and returns value of "num" key
# Use to order report nicely
def sort_on(characters_dict):
    return characters_dict["num"]

#sorts order of list_of_dics
list_of_dicts.sort(reverse=True, key=sort_on)


# cannot use 'dict' as it is reserved
# use 'item' instead and strings of value you want
# prints strings
for item in list_of_dicts:
    print(f"The {item['character']} character was found {item['num']} times")


# Prints end of report
print("--- End report ---")

