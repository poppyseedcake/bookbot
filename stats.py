def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for char in text:
        char = char.lower()
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    list_dict = []

    for key in dict:
        list_dict.append({"char": key, "num": dict[key]})

    sorted = list_dict.sort(reverse=True, key=sort_on)
    print(sorted)
    return sorted
