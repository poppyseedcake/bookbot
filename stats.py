def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for char in text:
        char = "'" + char.lower() + "'"
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters
