# -*- coding: UTF-8 -*-

# weight:物品重量，n:物品个数，w:背包可承载重量
def knapsack(weight:int, n: int, w: int):
    # 初始化状态表
    states = [0] * (w+1)
    states[0] = 1
    # 对于第一个物品
    if weight[0] <= w:
        states[weight[0]] = 1
    # 逐个考察所有物品
    for i in range(1, n):
        # 第i个物品放入背包
        for j in range(w-weight[i], -1, -1): # 注意此处j只能从大到小遍历
            if states[j]:
                states[j+weight[i]] = 1

    # 返回最大重量
    for i in range(w, -1, -1):
        if states[i]:
            return i
    return 0

if __name__ == '__main__':
    items = [2, 2, 6, 4, 3]
    n = len(items)
    w = 2
    result = knapsack(items, n, w)
    print(result)