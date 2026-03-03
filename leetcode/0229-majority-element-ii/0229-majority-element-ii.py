class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        count1, count2 = 0, 0

        for i, num in enumerate(nums):
            if not cand1:
                cand1 = num
                count1 = 1
                continue
            elif not cand2 and num != cand1:
                cand2 = num
                count2 = 1
                continue

            if count1 <= 0 and num != cand2:
                cand1 = num
                count1 = 0
            elif count2 <= 0 and num != cand1:
                cand2 = num
                count2 = 0

            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        if count1 <= 0 and nums[-1] != cand2:
            cand1 = nums[-1]
            count1 = 0
        elif count2 <= 0 and nums[-1] != cand1:
            cand2 = nums[-1]
            count2 = 0
        
        count1, count2 = 0, 0

        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
        
        ans = []

        if count1 > len(nums) // 3:
            ans.append(cand1)
        if count2 > len(nums) // 3:
            ans.append(cand2)
        
        return ans