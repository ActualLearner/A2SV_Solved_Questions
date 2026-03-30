class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()

        def find(path, index):
            if index == n and len(path) > 1:
                path_t = tuple(path)
                if path_t not in result:
                    result.add(path_t)
                return
            elif index == n:
                return
            
            if not path or nums[index] >= path[-1]:
                path.append(nums[index])
                find(path, index + 1)
                path.pop()

            find(path, index + 1)
        
        find([], 0)
        return [list(x) for x in result]