class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        left = 0

        max_q = deque()
        for i in range(k):
            
            while max_q and nums[i] > max_q[-1]:
                max_q.pop()

            max_q.append(nums[i])

        ans.append(max_q[0])

        for right in range(k, n):

            while max_q and nums[right] > max_q[-1]:
                max_q.pop()
            
            max_q.append(nums[right])

            while right - left + 1 > k:
                if max_q[0] == nums[left]:
                    max_q.popleft()
                left += 1
            
            ans.append(max_q[0])
        
        return ans