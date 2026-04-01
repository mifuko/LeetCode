### 用栈 天然有顺序
# 伪代码
# 按位置排序
# for 每个机器人:
#     if 方向是R:
#         push进栈
#     if 方向是L:
#         while 栈不为空 and 栈顶是R:
#             比较血量:
#                 L赢 → 弹出栈顶R，L血量-1，继续while
#                 R赢 → L死，R血量-1，break
#                 一样 → 两个都死，弹出栈顶R，break

# 最后栈里剩下的就是存活的机器人

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # 打包在一起按位置排序，保留原始index
        robots = sorted(zip(positions, healths, directions, range(len(positions))), key=lambda x: x[0])
        
        stack = []  # 存放往R走的机器人 [health, original_index]
        survivors = {}  # 存放所有存活的机器人 {original_index: health}
        
        for pos, health, direction, idx in robots:
            if direction == 'R':
                stack.append([health, idx])
            else:  # L
                health = health  # 当前L的血量
                while stack:
                    if stack[-1][0] < health:      # R血量少，R死
                        health -= 1
                        stack.pop()
                    elif stack[-1][0] > health:    # L血量少，L死
                        stack[-1][0] -= 1
                        health = 0
                        break
                    else:                          # 血量一样，两个都死
                        stack.pop()
                        health = 0
                        break
                
                if health > 0:  # L活下来了
                    survivors[idx] = health
        
        # 栈里剩下的R也是存活的
        for health, idx in stack:
            survivors[idx] = health
        
        # 按原始顺序输出
        return [survivors[i] for i in range(len(positions)) if i in survivors]