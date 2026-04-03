class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2

            if citations[mid] >= (n - mid):
                high = mid
            else:
                low = mid + 1

        return n - high if citations[high] != 0 else 0