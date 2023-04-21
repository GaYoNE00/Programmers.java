def solution(nums):
    max = set(nums)
    if len(max)>=len(nums)//2:
        return len(nums)//2
    return len(max)
