# -*- coding: UTF-8 -*-

maxW = -1  # 存储背包中物品总重量的最大值

# cw 表示当前装进去的物品重量和
# i 表示考察到哪个物品了
# w 背包重量
# items 表示每个物品的重量
# n 表示物品个数
# 函数调用方式cal01bag(0, 0, items, 10, 100)
def cal01bag(i, cw, items, n, w):
    global maxW
    # 装满了 or 装进了所有的物品
    if cw==w or i==n:
        if cw>maxW:
            maxW = cw
        return 
    # 第i个物品不放进背包
    cal01bag(i+1, cw, items, n, w)
    # 第i个物品放进背包
    if cw+items[i]<=w:
        cal01bag(i+1, cw+items[i], items, n, w)

if __name__ == '__main__':
    items = [2, 2, 3, 4, 5]
    cal01bag(0, 0, items, 5, 15)
    print(maxW)