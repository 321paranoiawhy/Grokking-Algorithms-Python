import random


# 双重for循环实现选择排序
def SelectionSort(arr):
    count = 0  # 记录交换/排序次数
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]  # 交换元素
        count += 1
        print("第 %d 次排序结果为: %s" % (count, arr))
    return arr


test_arr = random.sample([i for i in range(1, 10000)], 50)
print("最终升序排列结果为: %s" % SelectionSort(test_arr))
