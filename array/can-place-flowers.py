class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and \
                   (i == len(flowerbed)-1 or flowerbed[i+1] == 0):

                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True

        return n <= 0


# i == 0 当前位置是不是第一个位置？ 没有左邻居，所以不需要检查左边。
# flowerbed[i-1] == 0 左边的位置是不是空的？
# i == 0 or flowerbed[i-1] == 0 要么我在最左边，要么左边是空的。

# i == len(flowerbed)-1 当前位置是不是最后一个位置？
# flowerbed[i+1] == 0 右边的位置是不是空的？
# i == len(flowerbed)-1 or flowerbed[i+1] == 0 要么我在最右边，要么右边是空的。

# (左边条件) and (右边条件)
# \右斜杠只是换行无意义