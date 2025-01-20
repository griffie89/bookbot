def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"The book contains {word_count} words.")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()  # Split the text into a list of words
    return len(words)  # Return the length of the list (total words)

main()