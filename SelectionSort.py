import random


#  选择排序, 先定义最小值函数, 再定义选择排序函数(调用最小值函数), 以此对数组进行升序排列
#  定义函数, 输入数组arr, 返回其最小元素索引smallest_index
def find_smallest_element(arr):
    smallest_element = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
            smallest_index = i
    return smallest_index


test_arr = random.sample([i for i in range(1, 10000)],
                         20)  # 在1-9999范围内随机选取20个数作为test_arr
arr_origin = test_arr
print("数组 %s 中最小元素为: %d, 索引为: %d" %
      (test_arr, test_arr[find_smallest_element(test_arr)],
       find_smallest_element(test_arr)))


#  定义函数, 输入数组arr, 返回其升序排列new_arr
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        new_smallest_index = find_smallest_element(
            arr)  # 第 i 次查找arr中最小元素并获得其索引
        new_arr.append(
            arr.pop(new_smallest_index)
        )  # 每次循环将arr中删除(pop方法)的最小元素(arr长度逐次减1)依次添加(append方法)到new_arr中，循环完毕后获得升序排列
    return new_arr


print("上述数组升序排列为: %s" % selection_sort(test_arr))
