import numpy as np


class Frame:
    def __init__(self, piexls):
        # piexls 12x16 np数组
        self.piexls = piexls
        self.mean = np.mean(piexls)
        self.col_mean = self.colmean()
        self.col_diff = self.colCal_1()
        self.col_var = self.colCal_2()
        self.col_final = self.col_diff.copy() + self.col_var.copy()
        # # self.index = self.indexCal_1()
        self.index_list = self.indexCal_2()
        self.index = np.mean(self.index_list)

    def colmean(self):
        piexls = self.piexls
        col_mean = np.ones(16)
        for i in range(16):
            col_mean[i] = piexls[:, i].mean()
        return col_mean

    def indexCal_1(self):
        # 计算当前col_diff中值大于4的点的个数 一个点以下返回-1
        # 其他情况index值为代入权值的col：sum(col*col[i])/sum(col[i])
        col_list = self.col_var.copy()
        index = -1
        # print(col_list)
        count_above_1 = 0
        # print(np.max(col_list))
        for i in col_list:
            if i > 5:
                count_above_1 += 1

        if count_above_1 <= 1:
            return index
        col = 0
        sum1 = 0
        sum2 = 0
        for i in col_list:
            sum2 += i
            sum1 += col * i
            col += 1
        index = sum1 / sum2
        return round(index, 2)

    # 双人index
    def indexCal_2(self):
        col_list = self.col_final.copy()
        index = []
        count_above_1 = 0
        for i in range(16):
            if col_list[i] >= 5:
                count_above_1 += 1
            else:
                col_list[i] = -1
        if count_above_1 <= 1:
            return [-1]
        i = 0

        while i < 16:
            if col_list[i] > 0:
                sum_temp = 0
                sum_i = 0
                count_temp = 0
                while col_list[i] > 0:
                    count_temp += 1
                    sum_i += i * col_list[i]
                    sum_temp += col_list[i]
                    i += 1
                    if i == 16:
                        break
                if count_temp >= 2:
                    index.append(round(sum_i / sum_temp, 1))
            else:
                i += 1
        return index

    # debug1
    def colCal_1(self):
        piexls_mean = self.mean
        col_mean = self.col_mean
        col = np.ones(16)
        for i in range(16):
            col[i] = 4 * abs(col_mean[i] - piexls_mean)
        return col

    # debug2 方差
    def colCal_2(self):
        piexls1 = self.piexls
        b = np.ones(16)
        for i in range(16):
            b[i] = round(5 * np.var(piexls1[:, i]), 2)
        return b
