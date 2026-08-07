class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix[0]) - 1
        level_min = 0
        level_max = len(matrix) - 1
        mid = 0
        while level_min < level_max :
            mid = (level_max - level_min + 1) // 2 + level_min #borne sup
            if matrix[mid][0] > target :
                level_max = mid - 1
            elif matrix[mid][0] < target :
                level_min = mid
            else :
                return True
        
        while left < right :
            mid = (right - left + 1) // 2 + left
            if matrix[level_min][mid] > target :
                right = mid - 1
            elif matrix[level_min][mid] < target :
                left = mid
            else :
                return True
        print(mid, left, right, level_min)
        if matrix[level_min][right] == target :
            return True
        return False


        