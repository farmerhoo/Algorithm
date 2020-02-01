# -*- coding: UTF-8 -*-

# weight:物品重量，n:物品个数，w:背包可承载重量
def knapsack(weight:int, n: int, w: int):
    # 存放状态转移表
    states = [[0] * (w+1) for i in range(n)]
    # 处理初始数据
    states[0][0] = 1
    ## 动态规划的状态转移
    # 第一行
    if weight[0] < w:
        states[0][weight[0]] = 1
    for i in range(1, n):
        # 第i个物品不放入背包
        for j in range(w+1):
            if states[i-1][j]:
                states[i][j] = states[i-1][j]
        # 第i个物品放入背包
        for j in range(w+1-weight[i]):
            if states[i-1][j]:
                states[i][j+weight[i]] = 1
    # 返回结果
    for i in range(w, -1, -1):
        if states[n-1][i]:
            return i 
    return 0


    

if __name__ == '__main__':
    items = [2, 2, 6, 4, 3]
    n = len(items)
    w = 20
    result = knapsack(items, n, w)
    print(result)