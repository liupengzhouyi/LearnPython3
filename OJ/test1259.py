# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1259.py -*-
# -*- data: 2019-11-05 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1259


def paly(nowscore, index, answer):
    if index == 10:
        if nowscore == 100:
            print(answer)
    if index < 10:
        index = index + 1
        paly(nowscore * 2, index, str(answer + "1"))
        paly(nowscore - index, index, str(answer + "0"))
paly(10, 0, "")
