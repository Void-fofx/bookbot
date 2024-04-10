def get_word_count(text: str) -> int:
    return len(text.split())

def get_text(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

def main():
    path = "books/Frankenstein.txt"
    text = get_text(path)
    print(get_word_count(text))

if __name__ == "__main__":
    main()
