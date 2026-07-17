class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]

        for key, value in counter.items():
            arr[value].append(key)
        
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            if len(ans) == k:
                break

            while arr[i] and len(ans) < k:
                ans.append(arr[i].pop())
        
        return ans