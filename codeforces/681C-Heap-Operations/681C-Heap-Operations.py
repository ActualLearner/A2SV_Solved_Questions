from collections import defaultdict
def solve():
    n = int(input())
    hashmap = defaultdict(int)
    answer = []
    heap = []

    def heapify_up(arr, n, curr):
        parent = (curr - 1) // 2
        if parent >= 0 and arr[curr] < arr[parent]:
            arr[curr], arr[parent] = arr[parent], arr[curr]
            heapify_up(arr, n, parent)

    def heapify_down(arr, n, curr):
        left = (curr * 2) + 1 
        right = (curr * 2) + 2 
        max_ = curr

        if left < n and arr[left] < arr[max_]:
            max_ = left
        if right < n and arr[right] < arr[max_]:
            max_ = right
        
        if max_ != curr:
            arr[max_], arr[curr] = arr[curr], arr[max_]
            heapify_down(arr, n, max_)
    
    def heappush(arr, num):
        arr.append(num)
        heapify_up(arr, len(arr), len(arr) - 1)
    
    def heappop(arr):
        arr[0], arr[-1] = arr[-1], arr[0]
        heapify_down(arr, len(arr) - 1, 0)
        return arr.pop()

    for _ in range(n):
        data = input().split()
        opr = data[0]
        num = None if opr == "removeMin" else int(data[1])

        if opr == "insert":
            heappush(heap, num)
            hashmap[num] += 1
            answer.append([opr, str(num)])

        elif opr == "getMin":
            if hashmap[num] == 0:
                answer.append(["insert", str(num)])
                hashmap[num] += 1
                heappush(heap, num)

            while heap and heap[0] != num:
                val = heappop(heap)
                hashmap[val] -= 1
                answer.append(["removeMin"])

            answer.append([opr, str(num)])
            
        elif opr == "removeMin":
            if not heap:
                heappush(heap, 0)
                hashmap[0] += 1
                answer.append(["insert", "0"])
            
            val = heappop(heap)
            hashmap[val] -= 1
            answer.append(["removeMin"])

    print(len(answer))
    for i in answer:
        print(" ".join(i))
    

solve()