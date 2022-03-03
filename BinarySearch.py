from random import choice
import time
#  import random

start_time = time.time()


def binary_search(list, value):
    first = 0
    end = len(list) - 1
    count = 0

    while first <= end:
        mid = int((first + end) / 2)
        count = count + 1
        guess = list[mid]
        if guess > value:
            end = mid - 1
        elif guess < value:
            first = mid + 1
        else:
            end_time = time.time()
            time_wasted = end_time - start_time  # 记录程序运行时长
            print("二分法查找了 %d 次, 耗时 %.5f s, 即找到了目标值" %
                  (count, time_wasted))  # 输出程序运行时长(保留5位小数)
            return mid
    return None


str = list(range(1, 10000, 3))  # 创建1-10000的有序数组(步长3)
#  str = random.sample([i for i in range(1, 10000)], 100)  # 在1-10000的取值范围内随机取100个数作为str(无序)
print("有序列表为: %s" % str)  # 打印有序列表
random_value = choice(str)  # 在列表中随机取一个数random_value
print("目标值为: %d" % random_value)  # 打印目标值
print("目标值在列表中索引为: %d" % binary_search(str, random_value))  # 打印目标值在列表中的索引
