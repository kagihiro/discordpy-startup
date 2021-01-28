import random


def to_str_h_or_t(is_heads):
    return '表' if is_heads else '裏'


def get_str_by_flip_res(flip_res):
    # 結果を文字に変換する
    return to_str_h_or_t(flip_res == 1)


def toss_loop_until_prm(until_heads):
    # 指定した面が出るまで振る
    # until_heads == true　の時は表が出るまで(乱数でいうと1が出るまで)
    successes_count = -1
    res = -1
    while until_heads and not res == 1 or not until_heads and not res == 0:
        res = random.randint(0, 1)
        successes_count += 1
    return '{}が出るまで : {}回{}が出た'.format(to_str_h_or_t(until_heads), successes_count, to_str_h_or_t(not until_heads))


def toss(arg):
    # 1回振った結果
    if arg == '':
        flip_res = random.randint(0, 1)
        return get_str_by_flip_res(flip_res)

    # どっちかが出るまでの結果
    if arg == 'h' or arg == 't':
        return toss_loop_until_prm(arg == 'h')

    # 回数分振った結果
    times = int(arg)
    flip_res_list = [random.randint(0, 1) for x in range(times)]
    # 2d6  = (5+5) = 10
    # res = '{}回:({}) = 表{}回 , 裏{}回'.format(
    #     times, ','.join(map(str, flip_res_list)),
    #     sum([s == '表' for s in flip_res_list]),
    #     sum([s == '裏' for s in flip_res_list]))
    res = '{}回 : 表{}回 , 裏{}回'.format(
        times,
        sum([i == 0 for i in flip_res_list]),
        sum([i == 1 for i in flip_res_list]))
    return res
