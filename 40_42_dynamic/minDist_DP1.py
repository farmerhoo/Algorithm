# -*- coding: utf-8 -*-

'''
通过状态转移方程求解
'''
from typing import List

def min_dist_recur(weights: List[List[int]]) -> int:
    m, n = len(weights), len(weights[0])
    table = [[0] * n for _ in range(m)]
    def min_dist_to(i: int, j: int) -> int:
        if i == j == 0: 
            table[i][j] = weights[i][j]
            return weights[0][0]
        if table[i][j]: 
            return table[i][j]
        min_left = float("inf") if j - 1 < 0 else min_dist_to(i, j - 1)
        min_up = float("inf") if i - 1 < 0 else min_dist_to(i - 1, j)
        table[i][j] = weights[i][j] + min(min_left, min_up)
        return weights[i][j] + min(min_left, min_up)
    return min_dist_to(m - 1, n - 1)

if __name__ == '__main__':
    w = [[1, 3, 5, 9], 
         [2, 1, 3, 4], 
         [5, 2, 6, 7], 
         [6, 8, 4, 3]]
    result = min_dist_recur(w)
    print(result)