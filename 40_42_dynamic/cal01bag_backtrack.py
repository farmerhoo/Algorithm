# -*- coding: UTF-8 -*-

# 通过备忘录避免重复，提高回溯算法的效率
maxW = 0 # 存储背包能放置的最大重量
items = [2, 2, 4, 6, 3] # 物品的清单及重量
n = len(items)
w = 9  # 背包能承受的最大重量
mem = [[0] * (w+1) for i in range(n)]

def cal01bag(i: int, cw: int):
    global maxW, items, n, w, mem
    # 装满了 or 所有物品均已被考察
    if cw == w or i == n:
        if cw > maxW:
            maxW = cw
        return 
    # 重复状态
    if mem[i][cw]:
        return
    mem[i][cw] = 1
    # 第i个物品不放入背包
    cal01bag(i+1, cw)
    # 第i个物品放入背包
    if cw + items[i] <= w:
        cal01bag(i+1, cw+items[i])

if __name__ == '__main__':
    # print(mem)
    cal01bag(0, 0)
    print(maxW)