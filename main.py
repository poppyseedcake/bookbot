from stats import count_letters, count_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    words = count_words(book)
    print(f'{words} words found in the document')
    letters = count_letters(book)
    print(letters)


main()
