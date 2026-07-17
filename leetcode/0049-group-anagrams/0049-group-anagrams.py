class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = [0] * 26
        hashmap = defaultdict(list)

        for word in strs:
            count = arr[:]

            for char in word:
                idx = ord(char) - ord("a")
                count[idx] += 1
            
            hashmap[tuple(count)].append(word)
        
        return list(hashmap.values())