# -*- coding: utf-8 -*-

import sys

# items商品价格，n商品个数, w表示满减条件，比如200
def double11advance(items: list, n: int, w: int):
    # 初始化状态转移表
    states = [[0] * (3*w+1)] * n 
    # 考察第一个商品
    states[0][0] = 1
    if items[0] <= 3*w:
        states[0][items[0]] = 1
    # 逐个考察其他商品
    for i in range(1, n):
        # 第i个商品购买
        for j in range(3*w+1):
            if states[i-1][j] == 1:
                states[i][j] = 1
        # 第i个商品不购买
        for j in range(3*w+1-items[i]):
            if states[i-1][j]:
                states[i][j+items[i]] = 1
    
    # 输出结果大于等于w的最小值
    for j in range(w, 3*w+1):
        if states[n-1][j]:
            break  # 执行完后，j是大于等于w的最小值
    # 没有可行解
    if j == 3*w and states[n-1][j] != 1:
        print('最小的物品价格大于3倍优惠价格！！！')
        return 
    # 输出可行解
    for i in range(n-1, 0, -1):
        if j-items[i]>=0 and states[i-1][j-items[i]]==1:
            sys.stdout.write(str(items[i])+' ')
            j = j - items[i]

    if j != 0:
        sys.stdout.write(str(items[0]))

if __name__ == '__main__':
    items = [1, 6, 4, 2, 8]
    double11advance(items, len(items), 6)
