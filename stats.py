def word_count(book_contents):
    counter = 0
    word = book_contents.split()
    for i in word:
        counter += 1
    return counter


def character_count(book_contents):
    character_count = {}

    for char in book_contents:
        adj_char = char.lower()
        if adj_char in character_count:
            character_count[adj_char] += 1
        else:
            character_count[adj_char] = 1

    return character_count




# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries

test_dict = {"a":6546,"b":654,"c":654654}

def sort_on(items):
    return items["num"]

def dict_format(char_dict):
    new_output = []

    for key, value in char_dict.items():
        if key.isalpha():
            new_output.append({"char": key, "num": value})

    return sorted(new_output, key=sort_on, reverse=True)


print(dict_format(test_dict))







def sort_on(char_list):
return char_list["character_count"]

output = [
{"adj_char": "t", "character_count": 29493},
{"adj_char": "h", "character_count": 19176},
{"adj_char": "e", "character_count": 654654}
]
output.sort(reverse=True, key=sort_on)

print(output)


