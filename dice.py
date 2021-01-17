import random

# 回数無記入の場合の設定
default_times = 1
# 面数無記入の場合の設定
default_side = 6


def get_dice_info(message):
    # 無記入に対応
    if message == '':
        return [default_times, default_side]

    # 1d3 -> [1回,3面]
    times, side = message.split('d')
    # 回数無記入に対応
    if times == '':
        times = default_times
    # 面数無記入に対応
    if side == '':
        side = default_side
    return [int(times), int(side)]


def roll(message):
    times, side = get_dice_info(message)
    # ダイスを振った結果のリスト
    rand_res = [random.randint(1, side) for x in range(times)]
    # 2d6  = (5+5) = 10
    res = '{}d{} : ({}) = {}'.format(
        times, side, '+'.join(map(str, rand_res)), sum(rand_res))
    return res
