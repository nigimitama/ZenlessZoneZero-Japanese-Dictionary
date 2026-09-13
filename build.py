from pathlib import Path

from dict.words import RECORDS

FILE_WIN = Path("./zzz-dict-win.txt")
FILE_LIN = Path("./zzz-dict-mozc.txt")
FILE_MAC = Path("./zzz-dict-mac.txt")
RELEASE_NOTE = Path("./GENERATED_RELEASE_NOTE.md")


def generate_and_save_dict() -> None:
    with open(FILE_LIN, "w", encoding="utf-8") as f:
        f.writelines([f"{record.to_line_win()}\n" for record in RECORDS])
    with open(FILE_WIN, "w", encoding="utf-16") as f:
        f.writelines([f"{record.to_line_win()}\n" for record in RECORDS])
    with open(FILE_MAC, "w", encoding="utf-8") as f:
        f.writelines([f"{record.to_line_mac()}\n" for record in RECORDS])


def generate_and_save_release_note() -> None:
    contents = f"""
[Zenless Zone Zero](https://zenless.hoyoverse.com/) の日本語入力用の辞書です。

## 使用方法

1. 下記のAssetsからお使いのOSに合った辞書をダウンロードしてください
    - `{FILE_WIN.name}`：Windows用 (Microsoft IME / Google IME)
    - `{FILE_LIN.name}`：Linux用 (Mozc)
    - `{FILE_MAC.name}`：MacOS用
2. ダウンロードした `.txt` ファイルをご利用中のIMEにインポートしてください
""".strip()

    with open(RELEASE_NOTE, "w", encoding="utf-8") as f:
        f.write(contents)


if __name__ == "__main__":
    generate_and_save_dict()
    generate_and_save_release_note()
