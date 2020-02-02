# -*- coding: utf-8 -*-

def knapsack3(weight: list, value: list, w: int):
    
    n = len(weight) # 物品的个数
    # 初始化状态表
    states = [[-1] * (w+1) for i in range(n)]
    states[0][0] = 0
    # 考察第一个物品
    if weight[0] <= w:
        states[0][weight[0]] = value[0]

    # 依次考察剩余物品
    for i in range(1, n):
        # 第i个物品不放入
        for j in range(w+1):
            states[i][j] = states[i-1][j]

        # 第i个物品放入背包
        for j in range(w+1-weight[i]):
            if states[i-1][j] >= 0:
                v = states[i-1][j] + value[i]
                if v > states[i][j + weight[i]]:
                    states[i][j+weight[i]] = v
    
    # 找出最大值
    maxvalue = -1
    for i in range(w+1):
        if states[n-1][i] > maxvalue:
            maxvalue = states[n-1][i]
    return maxvalue

if __name__ == '__main__':
    items = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    result = knapsack3(items, values, 9)
    print(result)