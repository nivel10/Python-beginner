import os
# os.system('clear')
os.system('cls')

# --------------------------------------------
print('')

def find_first_sum(nums: list[int | float], goal: int | float) -> list[int | float]:

    nums_clone: list[int | float] = nums[:]
    index: int = 0

    for index_1 in range(len(nums)):
        for index_2 in range(index_1 + 1, len(nums)):
            if nums[index_1] + nums[index_2] == goal:
                return [index_1, index_2]
            
    return None

nums: list[int | float] = [0, 2, 2, 3, 5, 6]
# nums: list[int | float] = [0, 2, 2, 3, 5, 6]
goal: int | float = 8

result: int | float = 0
result = find_first_sum(nums=nums, goal=goal)
print(result)

print('')
result = find_first_sum(nums=nums, goal=19)
print(result)