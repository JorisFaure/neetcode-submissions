class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)

        while left < right :
            s = numbers[left - 1] + numbers[right - 1]
            if s == target :
                return [left, right]
            if s > target :
                right -=1
            elif s < target :
                left += 1
        return []
        