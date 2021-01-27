import random


def get_str_by_flip_res(flip_res):
    if (flip_res == 0):
        return ('裏')
    else:
        return ('表')


def toss(arg):
    # 引数なしの場合は1回振った結果を返し引数がある場合はその回数分振って返す
    if arg == '':
        flip_res = random.randint(0, 1)
        return get_str_by_flip_res(flip_res)

    times = int(arg)
    flip_res_list = [get_str_by_flip_res(
        random.randint(0, 1)) for x in range(times)]
    # 2d6  = (5+5) = 10
    res = '{}回:({}) = 表{}回 , 裏{}回'.format(
        times, ','.join(map(str, flip_res_list)),
        sum([s == '表' for s in flip_res_list]),
        sum([s == '裏' for s in flip_res_list]))
    return res
