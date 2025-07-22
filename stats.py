def word_count(book_contents):
    counter = 0
    words = book_contents.split()
    for word in words:
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


def sort_on(item):
    return item["num"]


def dict_format(char_dict):
    new_output = []

    for key, value in char_dict.items():
        if key.isalpha():
            new_output.append({"char": key, "num": value})

    return sorted(new_output, key=sort_on, reverse=True)
