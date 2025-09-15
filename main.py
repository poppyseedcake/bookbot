from stats import count_letters, count_words, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_out(words, list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {words} total words')
    print("--------- Character Count -------")
    for item in list:
       if item["char"].isalpha():
          print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

def main():
    book = get_book_text("books/frankenstein.txt")
    words = count_words(book)
    #print(f'{words} words found in the document')
    letters = count_letters(book)
    sorted = sort_dict(letters)

    print_out(words, sorted)

main()
