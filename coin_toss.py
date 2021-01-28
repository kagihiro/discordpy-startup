import random


def get_str_by_flip_res(flip_res):
    # 結果を文字に変換する
    if (flip_res == 0):
        return ('裏')
    else:
        return ('表')


def toss_loop_until_prm(until_heads):
    # 指定した面が出るまで振る
    # until_heads == true　の時は表が出るまで(乱数でいうと0が出るまで)
    successes_count = -1
    res = -1
    while until_heads and not res == 0 or not until_heads and not res == 1:
        res = random.randint(0, 1)
        successes_count += 1
    h_or_t = '表' if until_heads else '表'
    return '{}が出るまで振った結果 : {}回{}が出た'.format(h_or_t, successes_count, h_or_t)


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
    res = '{}回 = 表{}回 , 裏{}回'.format(
        times,
        sum([i == 0 for i in flip_res_list]),
        sum([i == 1 for i in flip_res_list]))
    return res
