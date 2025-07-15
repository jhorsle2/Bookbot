import os

# Set working directory to your project folder
os.chdir("C:/Python_Projects/Bookbot")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

main()
