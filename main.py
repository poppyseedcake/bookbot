from stats import count_letters, count_words, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_out(words, list, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f'Found {words} total words')
    print("--------- Character Count -------")
    for item in list:
       if item["char"].isalpha():
          print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    words = count_words(book)
    letters = count_letters(book)
    sorted = sort_dict(letters)

    print_out(words, sorted, book_path)

main()
