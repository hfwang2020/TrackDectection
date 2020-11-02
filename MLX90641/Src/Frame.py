import numpy as np


class Frame():
    def __init__(self, piexls):
        # piexls 12x16 np数组
        self.piexls = piexls
        self.piexls_mean = piexls.mean()
        self.col_mean = self.colmean()
        self.col_media = self.colmedia()
        self.col_diff = self.diff()
        
        self.col_var = self.colCal_2()
        self.index = self.indexCal_1()
        self.index_list = self.indexCal_2()
        print(self.index_list)
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
            col_diff[i] = abs(col[i%16]-col[(i+2)%16])
            +abs(col[i%16]-col[(i-1)%16])
            +abs(col[i%16]-col[(i-2)%16])
            +abs(col[i%16]-col[(i+1)%16])
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
        
        if count_above_4 <= 1:
            return index
        else:
            print(np.max(col_list),count_above_4)

        col = 0
        sum1 = 0
        sum2 = 0
        for i in col_list:
            sum2 += i
            sum1 += col * i
            col += 1
        index = sum1 / sum2
        return round(index, 2)
    
    def indexCal_1(self):
        # 计算当前col_diff中值大于4的点的个数 一个点以下返回-1
        # 其他情况index值为代入权值的col：sum(col*col[i])/sum(col[i])
        col_list = self.col_var
        index = -1
        # print(col_list)
        count_above_1 = 0
        # print(np.max(col_list))
        for i in col_list:
            if i > 1:
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
        col_list = self.col_var
        index = []
        count_above_1 = 0
        for i in range(16):
            if col_list[i] >= 1:
                count_above_1 += 1
            else :
                col_list[i] = -1   
        if count_above_1 <= 1:
            return [-1]
    
        i = 0
        sum_i = 0
        sum_temp = 0
        
        while(i<16):
            if col_list[i]>0:
                sum_temp = 0
                sum_i = 0
                while(col_list[i]>0 ):
                    sum_i += i*col_list[i]
                    sum_temp+=col_list[i]
                    i += 1
                    if i == 16:
                        break
                index.append(sum_i/sum_temp)
            else:
                i += 1

        return index

    # debug1
    def colCal_1(self):
        piexls_mean = self.piexls_mean
        col_mean = self.col_mean
        col = np.ones(16)
        for i in range(16):
            col[i] = 4*abs(col_mean[i] - piexls_mean)
        return col

    # debug2 方差
    def colCal_2(self):
        piexls = self.piexls
        b=np.ones(16)
        for i in range(16):
            b[i] = round(np.var(piexls[:,i]),2)
        return b