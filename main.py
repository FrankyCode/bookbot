from stats import get_num_words, get_count_characters, sort_dictionary_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def generate_report(file_path, total_words, sorted_dictionary_charts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for character in sorted_dictionary_charts:
        if character.isalpha():
            print(f"{character}: {sorted_dictionary_charts[character]}")
    print("============= END ===============")


def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    character_dictionary = get_count_characters(book_text)
    sorted_dictionary = sort_dictionary_list(character_dictionary)
    generate_report(file_path, num_words, sorted_dictionary)

main()