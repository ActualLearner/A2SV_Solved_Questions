class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups_to_nodes = defaultdict(list)
        curr_empty = m
        adj = defaultdict(list)
        adj_nodes = defaultdict(list)
        indeg_nodes = [0] * n
        indeg = [0] * (m + n)

        for i in range(n):
            if group[i] == -1:
                while groups_to_nodes[curr_empty]:
                    curr_empty += 1 

                group[i] = curr_empty

            groups_to_nodes[group[i]].append(i)
        

        seen = defaultdict(set)
        for i in range(n):
            if not beforeItems[i]:
                continue

            curr_group = group[i]

            for idx in beforeItems[i]:
                if group[idx] == curr_group:
                    adj_nodes[idx].append(i)
                    indeg_nodes[i] += 1
                    continue

                if group[idx] not in seen[curr_group]:
                    adj[group[idx]].append(curr_group)
                    indeg[curr_group] += 1
                    seen[curr_group].add(group[idx])

        groups_sorted = []
        queue = deque([i for i in groups_to_nodes if indeg[i] == 0])
        while queue:
            curr = queue.popleft()
            groups_sorted.append(curr)

            for nei in adj[curr]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
        
        if len(groups_sorted) < len(groups_to_nodes):
            return []

        ans = []
        for g in groups_sorted:
            nodes = groups_to_nodes[g]
            queue = deque([i for i in nodes if indeg_nodes[i] == 0])
            batch = []

            while queue:
                curr = queue.popleft()
                batch.append(curr)

                for nei in adj_nodes[curr]:
                    indeg_nodes[nei] -= 1
                    if indeg_nodes[nei] == 0:
                        queue.append(nei)

            if len(batch) < len(nodes):
                return []
            
            ans.extend(batch)
        
        return ans