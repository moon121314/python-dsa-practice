def remove_duplicate(nums):
    new_nums = set(nums)
    return list(new_nums)

nums = [1, 2, 2, 3, 1, 4]
print(remove_duplicate(nums))

time com : 0(1)
space : 0(1)