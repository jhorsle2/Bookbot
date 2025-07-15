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


