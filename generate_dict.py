from dict.words import WORDS, ITEMS, PARTIES, CHARACTERS


if __name__ == "__main__":
    FILE = "./ZZZ-Japanese-Dict-Windows.txt"
    records = sum([WORDS, ITEMS, PARTIES, CHARACTERS], [])
    with open(FILE, "w", encoding="utf-8") as f:
        f.writelines([f"{record.to_line()}\n" for record in records])
