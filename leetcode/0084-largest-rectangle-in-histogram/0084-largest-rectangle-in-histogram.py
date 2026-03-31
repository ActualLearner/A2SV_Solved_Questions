class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_ = 0
        hashmap1 = {}
        hashmap2 = {}

        stack1 = []
        stack2 = []

        for i, num in enumerate(heights):
            
            while stack1 and heights[stack1[-1]] >= num:
                idx = stack1.pop()
                if idx not in hashmap1:
                    hashmap1[idx] = -1

            if stack1 and heights[stack1[-1]] < num:
                idx = stack1[-1]
                hashmap1[i] = idx
            
            stack1.append(i)

            while stack2 and heights[stack2[-1]] > num:
                idx = stack2.pop()
                hashmap2[idx] = i
            
            stack2.append(i)

        while stack1:
            idx = stack1.pop()
            if idx not in hashmap1:
                hashmap1[idx] = -1

        while stack2:
            idx = stack2.pop()
            hashmap2[idx] = n
        

        for i in range(n):
            area = (hashmap2[i] - hashmap1[i] - 1) * heights[i]
            print(area, heights[i], [hashmap1[i], hashmap2[i]])
            max_ = max(max_, area)
        
        return max_