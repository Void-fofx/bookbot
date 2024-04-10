def print_report(book_title: str, letter_counts: list, word_count: int) -> None:
    print(f"------ Begin report for {book_title} ------\n")
    print(f"Total words: {word_count}\n")
    print("--- Letter frequency ---")
    for letter in letter_counts:
        print(f"Letter '{letter['letter']}': {letter['count']}")

def sort_on(dictionary: dict) -> int:
    return dictionary["count"]

def sort_letter_counts(letter_counts: dict) -> list:
    list_of_dicts = []
    for letter in letter_counts:
        list_of_dicts.append({"letter": letter, "count": letter_counts[letter]})
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts

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
    sorted = sort_letter_counts(letter_counts)
    word_count = get_word_count(text)
    print_report("Frankenstein", sorted, word_count)

if __name__ == "__main__":
    main()
