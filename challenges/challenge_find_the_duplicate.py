def find_duplicate(nums):
    if (len(nums) <= 1):
        return False
    nums.sort()
    for index in range(len(nums) -1):
        number = nums[index]
        next_number = nums[index + 1]
        if (
            type(number) is not int
            or number < 0
        ):
            return False
        if number == next_number:
            return number
    
    return False
