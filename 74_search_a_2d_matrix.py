class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return target
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        m = len(matrix)
        n = len(matrix[0])

        row_to_bs = 0
        for row in range(m):
            if matrix[row][0] <= target and target <= matrix[row][n - 1]:
                row_to_bs = row
                break

        result = binary_search(matrix[row_to_bs], target)
        return result != -1
