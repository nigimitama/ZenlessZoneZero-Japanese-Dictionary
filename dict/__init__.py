from dataclasses import dataclass
from enum import Enum


class Category(Enum):
    """Windows IMEだと「品詞」、Google IMEだと「カテゴリ」と呼ばれるもの"""

    NOUN = "名詞"
    NAME = "人名"
    LOCATION = "地名その他"


def category_win_to_mac(category: str):
    """Mac用の品詞名にする

    ref: https://support.apple.com/ja-jp/guide/japanese-input-method/jpim10226/mac
    """
    if category == Category.NOUN.value:
        return "普通名詞"
    if category == Category.LOCATION.value:
        return "地名"
    return category


@dataclass
class Record:
    reading: str
    word: str
    category: Category
    category_str: str = ""
    comment: str = ""

    def __post_init__(self) -> None:
        if isinstance(self.category, Category):
            self.category_str: str = self.category.value

    def to_line_win(self) -> str:
        """タブ区切りの1行に整形する"""
        return f"{self.reading}\t{self.word}\t{self.category_str}\t{self.comment}"

    def to_line_mac(self) -> str:
        """タブ区切りの1行に整形する"""
        return f"{self.reading}\t{self.word}\t{category_win_to_mac(self.category_str)}"
