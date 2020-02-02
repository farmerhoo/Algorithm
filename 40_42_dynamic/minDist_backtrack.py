# -*- coding: utf-8 -*-

# 全局变量
minDist = 100

def minDistBT(i: int, j: int, dist: int, w: list):
    global minDist
    n = len(w)
    # 结束递归的基线条件
    # 到了终点
    if i==n-1 and j==n-1:
        if dist+w[i][j]<minDist:
            minDist = dist + w[i][j]
        return 
    # 往下走，更新i=i+1, j=j
    if i < n-1:
        minDistBT(i+1, j, dist+w[i][j], w)
    # 往右走，更新i=i, j=j+1
    if j < n-1:
        minDistBT(i, j+1, dist+w[i][j], w)

if __name__ == '__main__':
    w = [[1, 3, 5, 9], 
         [2, 1, 3, 4], 
         [5, 2, 6, 7], 
         [6, 8, 4, 3]]
    minDistBT(0, 0, 0, w)
    print(minDist)