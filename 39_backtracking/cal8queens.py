import numpy as np
solution_count = 0 # 全局变量，存放所有的解
result = [0]*8 # 全局变量，下标表示行，值表示queen储存在哪一列
def cal8queen(row: int):
    '''
    Args:
        row(int) - 放棋子的行
    Return:
        none
    '''
    global solution_count
    # 8个棋子都已经放好了
    if row>=8:
        printQueens(result)
        # print(result)
        solution_count += 1
        return
    # 每一行有8种放置方法
    for column in range(8):
        # 有些放法不满足要求
        if isOK(row, column)==True:
            result[row] = column # 第row行放置到第column列
            cal8queen(row+1)

def isOK(row, column):
    '''
    Arg:
        row(int) - 放置棋子的行
        column(int) - 放置棋子的列
    Return:
        判断row行column列放置棋子是否合适
    '''
    leftup = column - 1
    rightup = column + 1
    # 逐行向上考察
    for i in range(row-1, -1, -1):
        # 第i行的column列有棋子
        if result[i] == column:
            return False
        # 考察左上对角线
        if leftup>=0:
            if result[i] == leftup:
                return False
        # 考察右上对角线
        if rightup<8:
            if result[i] == rightup:
                return False
        leftup -= 1
        rightup += 1

        # 考察对角线
        # if abs(column - result[i]) == row - i:
        #     return False
    return True

def printQueens(result):
    '''
    打印二维矩阵
    '''
    queens = np.zeros([8, 8])
    for row in result:
        queens[row][result[row]] = 1
    print(queens)
        
if __name__ == '__main__':
    cal8queen(0)
    print(solution_count)