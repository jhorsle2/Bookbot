import os

os.chdir(r'C:\Python_Projects\Bookbot')

from stats import word_count,character_count,sort_on


def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    words = word_count(text)
    characters = character_count(text)
    print(f'{words} words found in the document')
    print(characters)
    print(characters.items())


def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()





main()

