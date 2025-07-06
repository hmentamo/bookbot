# main.py
# This is the main file that runs the program.
# It imports the functions from the stats.py file and uses them to analyze the book.
# It then prints the results to the console.

import sys

from stats import count_words, get_book_text
from stats import count_characters, sort_characters


def main():
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line argument
    path_to_file = sys.argv[1]
    book_content = get_book_text(path_to_file)
    word_count = count_words(book_content)
    characters = count_characters(book_content)
    sorted_characters = sort_characters(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_characters:
        print(f"{char_dict['char']}: {char_dict['count']}")

    print("============= END ===============")


main()
