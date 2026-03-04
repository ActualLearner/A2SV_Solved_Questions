class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort()
        ans = 0
        h = 1

        for i in range(N - 1, -1, -1):
            if citations[i] >= h:
                ans = h

            h += 1

        return ans