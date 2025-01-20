def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # Generate word and character data
    word_count = count_words(text)
    char_counts = count_characters(text)
    
    # Generate the report
    generate_report(book_path, word_count, char_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()  # Convert all characters to lowercase
    char_count = {}
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count


def generate_report(book_path, word_count, char_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Sort the character counts by frequency in descending order
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


main()
