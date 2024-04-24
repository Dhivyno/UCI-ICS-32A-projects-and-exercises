from time import time
import random

def find_max(nums: list[int], length) -> int:
    if length == 1:
        return nums[0]
    return max(nums[length - 1], find_max(nums, length - 1))

def find_max2(nums: list[int]) -> int:
    largest = None

    for num in nums:
        if largest == None or num > largest:
            largest = num

    return largest


if __name__ == "__main__":
    num_list = []
    for i in range(998):
        num_list.append(random.randint(1, 10000))
    length = len(num_list)
    start_time = time()
    print(find_max(num_list, length))
    end_time = time()
    print(end_time-start_time)
    
    start_time = time()
    print(find_max2(num_list))
    end_time = time()
    print(end_time-start_time)

