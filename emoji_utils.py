from enum import Enum


class Emoji(Enum):
    # 絵文字の判断に使う

    WIN = 0
    LOSE = 1
    NONE = -1


def get_emoji_enum(emoji_str):

    if emoji_str == '':
        return Emoji.WIN
    elif emoji_str == '':
        return Emoji.LOSE
    else:
        return Emoji.NONE


def to_emoji(reaction):
    return reaction.emoji
