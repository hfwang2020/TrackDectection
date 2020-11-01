import numpy as np


class Frame():
    def __init__(self, piexls):
        # piexls 12x16 np数组
        self.piexls = piexls
        self.piexls_mean = piexls.mean()
        self.col_mean = self.colmean()
        self.col_media = self.colmedia()
        self.col_diff = self.diff()
        self.index_list = self.points_index()
        self.index = self.indexCal()
        # self.index = self.index_list_to_index()
        # self.index = np.mean(self.index_list)

    def colmean(self):
        piexls = self.piexls
        col_mean = np.ones(16)
        for i in range(16):
            col_mean[i] = piexls[:, i].mean()
        return col_mean

    def colmedia(self):
        piexls = self.piexls
        col_media = np.ones(16)
        for i in range(16):
            col_media[i] = np.median(piexls[:, i])
            # col_media[i] = piexls[:, i].median()
        return col_media

    def diff(self):
        col = self.col_mean
        # col = self.col_media
        col_diff = np.ones(16)
        col_diff[0] = abs(4 * col[0] - col[1] - col[2] - 2 * self.piexls_mean)
        col_diff[1] = abs(4 * col[1] - col[2] - col[3] - 2 * self.piexls_mean)
        col_diff[14] = abs(4 * col[14] - col[12] - col[13] - 2 * self.piexls_mean)
        col_diff[15] = abs(4 * col[15] - col[14] - col[13] - 2 * self.piexls_mean)
        for i in range(2, 14):
            # col_diff[i] = abs(4 * col[i % 16] - col[(i + 1) % 16] - col[(i - 1) % 16] - col[(i + 2) % 16] - col[
            #     (i - 2) % 16])
            col_diff[i] = abs(col[i%16]-col[(i+2)%16])+abs(col[i%16]-col[(i-1)%16])+abs(col[i%16]-col[(i-2)%16])+abs(col[i%16]-col[(i+1)%16])
        # col_diff[0] = 0
        # col_diff[-1] = 0
        return col_diff

    # 可以改进的地方加入list里面值的权重
    def points_index(self):
        col = self.col_diff
        index_list = []
        # 列表极大点和差值大于2的点列坐标 -> 异常点
        for i in range(2, 14):
            # if ((col[i] > col[i - 1] and col[i] > col[i + 1]) and (col[i] > 2)):
            if col[i] > 2:
                index_list.append(i)
        return index_list
        # 当前帧无异常点，返回 -1

    def index_list_to_index(self):
        index_list = self.index_list
        index = -1
        if index_list.__len__() == 0:
            index = -1
        else:
            index = np.mean(index_list)
        # 双人算法优化index
        # elif index_list.__len__() == 3:
        #     if abs(index_list[0] - index_list[-1]) <= 5:
        #         index = np.mean(index_list)
        # else:
        #     index = np.mean(index_list)
        return index

    def indexCal(self):
        # 计算当前col_diff中值大于4的点的个数 一个点以下返回-1
        # 其他情况index值为代入权值的col：sum(col*col[i])/sum(col[i])
        col_list = self.col_diff
        index = -1
        # print(col_list)
        count_above_4 = 0
        # print(np.max(col_list))
        for i in col_list:
            if i > 4:
                count_above_4 += 1
        print(np.max(col_list),count_above_4)
        if count_above_4 <= 1:
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