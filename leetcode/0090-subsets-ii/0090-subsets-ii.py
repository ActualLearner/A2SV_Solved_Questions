class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        hashmap = Counter(nums)
        nums = list(hashmap.keys())
        n = len(nums)
        result = []

        def subset(path, index):
            if index == n:
                result.append(path[:])
                return

            for i in range(1, hashmap[nums[index]] + 1):
                l = len(path)
                path.extend([nums[index]] * i)
                subset(path, index+1)
                path = path[:l]
                print(path)

            subset(path, index + 1)

        subset([], 0)
        return result