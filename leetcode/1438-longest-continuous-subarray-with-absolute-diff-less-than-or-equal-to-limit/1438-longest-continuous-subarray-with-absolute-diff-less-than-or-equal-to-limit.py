class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        
        ans = 0
        left = 0
        max_q = deque()
        min_q = deque()

        for right in range(n):
            # add to queues
            while max_q and max_q[-1] < nums[right]:
                max_q.pop()
            
            max_q.append(nums[right])

            while min_q and min_q[-1] > nums[right]:
                min_q.pop()
            
            min_q.append(nums[right])

            # while invalid
            while left <= right and max_q[0] - min_q[0] > limit:
                if nums[left] == max_q[0]:
                    max_q.popleft()
                if nums[left] == min_q[0]:
                    min_q.popleft()

                left += 1 

            # add to answer
            ans = max(ans, right - left + 1)
        
        return ans