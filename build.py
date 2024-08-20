from pathlib import Path
from dict.words import WORDS, ITEMS, PARTIES, CHARACTERS

FILE_WIN = Path("./zzz-dict-win.txt")
FILE_MAC = Path("./zzz-dict-mac.txt")
RELEASE_NOTE = Path("./GENERATED_RELEASE_NOTE.md")


def generate_dict():
    records = sum([WORDS, ITEMS, PARTIES, CHARACTERS], [])
    with open(FILE_WIN, "w", encoding="utf-8") as f:
        f.writelines([f"{record.to_line_win()}\n" for record in records])
    with open(FILE_MAC, "w", encoding="utf-8") as f:
        f.writelines([f"{record.to_line_mac()}\n" for record in records])


def generate_release_note():
    contents = f"""
[Zenless Zone Zero](https://zenless.hoyoverse.com/) の日本語入力用の辞書です。

# 使用方法

1. 下記のAssetsから `{FILE_WIN.name}` あるいは `{FILE_MAC.name}` をダウンロードしてください
2. ご利用中のIMEに辞書をインポートしてください
""".strip()

    with open(RELEASE_NOTE, "w", encoding="utf-8") as f:
        f.write(contents)


if __name__ == "__main__":
    generate_dict()
    generate_release_note()