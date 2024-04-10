def print_report(book_title: str, letter_counts: dict, word_count: int) -> None:
    print(f"------ Begin report for {book_title} ------\n")
    print(f"Total words: {word_count}\n")
    print("--- Letter frequency ---")
    for letter, count in letter_counts.items():
        print(f"Letter '{letter}': {count}")

def get_letter_count(text: str) -> dict:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    letter_counts = {}
    for letter in text:
        if letter in alphabet:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts


def get_word_count(text: str) -> int:
    return len(text.split())

def get_text(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

def main():
    path = "books/Frankenstein.txt"
    text = get_text(path)
    letter_counts = get_letter_count(text)
    word_count = get_word_count(text)
    print_report("Frankenstein", letter_counts, word_count)

if __name__ == "__main__":
    main()
