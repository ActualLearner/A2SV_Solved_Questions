class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        size = rows * cols

        low, high = 0, size - 1
        while low <= high:
            mid = (low + high) // 2
            i = mid // cols
            j = mid % cols

            if matrix[i][j] > target:
                high = mid - 1
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                return True
        
        return False
