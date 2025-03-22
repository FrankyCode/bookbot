def get_num_words(string_book):
    num_words = len(string_book.split())
    return num_words

def get_count_characters(string_book):
    character_dictionary = {}
    convert_to_lowercase = string_book.lower()
    list_text = list(convert_to_lowercase)
    for letter in list_text:
        if letter in character_dictionary:
            character_dictionary[letter] += 1
        else:
            character_dictionary[letter] = 1

    return character_dictionary

def sort_dictionary_list(character_dictionary):
    return dict(sorted(character_dictionary.items(), key=lambda item: item[1], reverse=True))