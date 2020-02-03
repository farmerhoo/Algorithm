# -*- coding: utf-8 -*-

# 回溯算法实现
def levenshteinBT(s1: str, s2: str) -> int:
    n1 = len(s1)
    n2 = len(s2)
    minDist = 999999
    # backtracking
    def bt_algo(i: int, j: int, edist: int):
        '''
        Args:
            i(int) - 字符串1考察的位置;
            j(int) - 字符串2考察的位置;
            edist(int) - 编辑的次数
        '''
        # 递归的基线条件
        if i==n1 or j==n2:
            nonlocal minDist
            if i < n1:
                edist += n1 - i
            if j < n2:
                edist += n2 - j
            if edist < minDist:
                minDist = edist
            return 
        # 递归条件
        # 考察位置的字符相同
        if s1[i] == s2[j]:
            bt_algo(i+1, j+1, edist)
        # 考察位置的字符不相同
        else:
            bt_algo(i+1, j, edist+1) # 删除第i个字符
            bt_algo(i, j+1, edist+1) # 删除第j个字符
            bt_algo(i+1, j+1, edist+1) # 将s1[i]和s2[j]替换为相同的字符
    bt_algo(0, 0, 0)
    return minDist

# 动态规划算法实现
'''
状态表的递推公式：
如果：a[i]!=b[j]，那么：min_edist(i, j)就等于：
min(min_edist(i-1,j)+1, min_edist(i,j-1)+1, min_edist(i-1,j-1)+1)
如果：a[i]==b[j]，那么：min_edist(i, j)就等于：
min(min_edist(i-1,j)+1, min_edist(i,j-1)+1，min_edist(i-1,j-1))
'''
def levenshteinDP(s1: str, s2: str) -> int:
    n1 = len(s1)
    n2 = len(s2)
    # 定义状态表
    table = [[-1] * n2 for i in range(n1)]
    # 初始化状态表的第0行, s1[0...0]和s2[0...j]的编辑距离
    for j in range(n2):
        if s1[0] == s2[j]:
            table[0][j] = j
        elif j != 0:
            table[0][j] = table[0][j-1] + 1
        else:
            table[0][j] = 1
    # 初始化第0列:s1[0..i]与s2[0..0]的编辑距离
    for i in range(n1):
        if s1[i] == s2[0]:
            table[i][0] = i 
        elif i != 0:
            table[i][0] = table[i-1][0]+1
        else:
            table[i][0] = 1
    # 按行填表
    for i in range(1, n1):
        for j in range(1, n2):
            if s1[i] == s2[j]:
                table[i][j] = min(table[i-1][j]+1, table[i][j-1]+1, table[i-1][j-1])
            else:
                table[i][j] = min(table[i-1][j]+1, table[i][j-1]+1, table[i-1][j-1]+1)
    return table[n1-1][n2-1]


if __name__ == '__main__':
    s1 = 'eeee'
    s2 = 'eeee'
    result = levenshteinBT(s1, s2)
    print(result)
    result1 = levenshteinDP(s1, s2)
    print(result1)


