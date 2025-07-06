def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters


def sort_characters(characters):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in characters.items():
        char_list.append({"char": char, "count": count})

    # Sort by count in descending order
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(item):
    return item["count"]
