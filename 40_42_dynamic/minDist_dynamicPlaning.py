# -*- coding: utf-8 -*-

def minDistDP(matrix: list, n):
    # 初始化状态转移表
    states = [[100] * n for i in range(n)]
    sum = 0
    # 初始化状态表第一行
    for j in range(n):
        sum += matrix[0][j]
        states[0][j] = sum
    # 初始化状态表第一列
    sum = 0
    for i in range(n):
        sum += matrix[i][0]
        states[i][0] = sum 
    # 从第二行开始逐行考察数据
    for i in range(1, n):
        for j in range(1, n):
            states[i][j] = min([states[i-1][j]+matrix[i][j], states[i][j-1]+matrix[i][j]])
    # 获取返回值
    return states[n-1][n-1]

if __name__ == '__main__':
    w = [[1, 3, 5, 9], 
         [2, 1, 3, 4], 
         [5, 2, 6, 7], 
         [6, 8, 4, 3]]
    result = minDistDP(w, len(w))
    print(result)