def find_duplicate(nums):
    if (len(nums) <= 1):
        return False
    nums.sort()
    for number in nums:
        if (
            type(number) != int
            or number < 0
        ):
            return False
    return True
