from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = findFirstElement_rightInclusive(nums, target)
        end = findLastElement_rightInclusive(nums, target)
        return [start, end]


def findFirstElement_rightInclusive(nums, target):
    """
    * during each itertaion nums[right] is processed (inclusive)
    * left points to the first element of target (if exist)
    * termination condition should include left == right, at the end of the for loop left == right + 1
    * if nums[mid] < target: 
        left = mid + 1 because nums[:mid+1] has been processed
        if target is larger than all elements, left becomes len(nums) so we need to check left == len(nums) before return
        or we can add it as a fast check before the while loop:
        if target > nums[1]:
            return -1
    * if nums[mid] > target:
        right = mid - 1 because nums[mid:] has been processed
    * if nums[mid] == target:
        left = mid + 1 because we are looking for the left bound of target
        ** interestingly if nums[mid] is the first element of target, from the next iteration:
            right = index of first element - 1, and then left keeps moving towards right until left == right
            then left becomes right + 1, which is the answer
    * condition nums[mid] > target & nums[mid] == target can be merged
    """
    if len(nums) == 0:
        return -1
    # if target > nums[-1]:
    #     return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == len(nums) or nums[left] != target:
    # if nums[left] != target:
        return -1
    else:
        return left

def findLastElement_rightInclusive(nums, target):
    """
    * during each itertaion nums[right] is processed (inclusive)
    * right points to the last element of target (if exist)
    * termination condition should include left == right, at the end of the for loop left == right + 1
    * if nums[mid] > target: 
        right = mid - 1 because nums[mid:] has been processed
        if target is smaller than all elements, right becomes -1 so we need to check right == -1 before return
        or we can add it as a fast check before the while loop:
        if target < nums[0]:
            return -1
    * if nums[mid] < target:
        left = mid + 1 because nums[:mid+1] has been processed
    * if nums[mid] == target:
        left = mid + 1 because we are looking for the right bound of target
        ** interestingly if nums[mid] is the last element of target, from the next iteration:
            left = index of last element + 1, and right keeps moving towards left until right == left
            then right becomes left - 1, which is the answer
    * condition nums[mid] < target & nums[mid] == target can be merged
    """
    if len(nums) == 0:
        return -1
    # if nums[0] > target:
    #     return -1
    left = 0
    right = len(nums) - 1 
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if right == -1 or nums[right] != target:
    # if nums[right] != target:
        return -1
    else:
        return right
