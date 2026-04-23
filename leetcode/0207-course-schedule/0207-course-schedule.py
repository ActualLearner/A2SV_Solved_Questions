class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for v, u in prerequisites:
            adj_list[u].append(v)

        color = [0] * numCourses

        def dfs(node):
            if color[node] == 1:
                return False
            elif color[node] == 2:
                return True
            
            color[node] = 1

            for n in adj_list[node]:
                if not dfs(n):
                    return False
            
            color[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        