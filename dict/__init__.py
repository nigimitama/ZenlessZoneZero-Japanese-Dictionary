from enum import Enum
from dataclasses import dataclass


class Category(Enum):
    NOUN = "名詞"
    NAME = "人名"
    LOCATION = "地名"
    OTHER = "その他"


def category_win_to_mac(category: str):
    """Mac用の品詞名にする

    ref: https://support.apple.com/ja-jp/guide/japanese-input-method/jpim10226/mac
    """
    if category == Category.NOUN.name:
        return "普通名詞"
    return category


@dataclass
class Record:
    reading: str
    word: str
    category: str | Category = "名詞"  # category: Windows IMEだと「品詞」、Google IMEだと「カテゴリ」
    comment: str = ""

    def __post_init__(self) -> None:
        if isinstance(self.category, Category):
            self.category: str = self.category.value

    def to_line_win(self) -> str:
        """タブ区切りの1行に整形する"""
        return "\t".join([
            self.reading,
            self.word,
            self.category,
            self.comment
        ])

    def to_line_mac(self) -> str:
        """タブ区切りの1行に整形する"""
        return "\t".join([
            self.reading,
            self.word,
            category_win_to_mac(self.category),
        ])
