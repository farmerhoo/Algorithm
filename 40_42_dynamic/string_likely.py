# -*- coding: utf-8 -*-

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
            bt_algo(i+1, i+2, edist)
        # 考察位置的字符不相同
        else:
            bt_algo(i+1, j, edist+1) # 删除第i个字符
            bt_algo(i, j+1, edist+1) # 删除第j个字符
            bt_algo(i+1, j+1, edist+1) # 将s1[i]和s2[j]替换为相同的字符
    bt_algo(0, 0, 0)
    return minDist

if __name__ == '__main__':
    s1 = 'mitcmu'
    s2 = 'mtacnu'
    result = levenshteinBT(s1, s2)
    print(result)


