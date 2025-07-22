##import os
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Set working directory
##os.chdir(r'C:\Python_Projects\Bookbot')

# Import helper functions
from stats import word_count, character_count, sort_on, dict_format

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    book_path = book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = word_count(text)
    characters = character_count(text)
    final_output = dict_format(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {words} total words')
    print("--------- Character Count -------")
    for item in final_output:
        print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

# Run the program
main()
