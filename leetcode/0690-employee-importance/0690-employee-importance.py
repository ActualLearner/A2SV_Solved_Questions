"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adj = defaultdict(list)
        weights = [0] * 2001
        root = None

        for emp in employees:
            adj[emp.id].extend(emp.subordinates)
            weights[emp.id] = emp.importance

            if emp.id == id:
                root = emp
        

        under = []
        queue = deque([root.id])
        vis = set()

        while queue:
            node = queue.popleft()
            under.append(node)

            for nei in adj[node]:
                if nei in vis:
                    continue
                
                vis.add(nei)
                queue.append(nei)

        ans = 0
        for node in under:
            ans += weights[node]

        return ans