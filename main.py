import os

os.chdir(r'C:\Python_Projects\Bookbot')



def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    words = word_count(text)
    print(words)


def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def word_count(book_contents):
    counter = 0
    word = book_contents.split()
    for i in word:
        counter += 1
    return counter



main()

