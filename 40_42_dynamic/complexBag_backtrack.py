# -*- coding: utf-8 -*-

def f(i, cw, cv):
    '''
    i(int) - 第i个物品
    cw(int) - 背包目前的重量
    cv(int) - 背包目前的价值
    '''
    global maxV, items, values, w
    n = len(items)
    # 装满了 or 考察所有物品
    if cw==w or i==n:
        if cv > maxV:
            maxV = cv
        return 
    # 第i个物品不放入背包
    f(i+1, cw, cv)
    # 第i个物品放入背包
    if cw + items[i] <= w:
        f(i+1, cw+items[i], cv+values[i])

if __name__ == '__main__': 
    maxV = 0 # 存放背包能放置的最大物品价值
    items = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    w = 9 # 背包能承受的最大重量
    f(0,0,0)
    print(maxV)