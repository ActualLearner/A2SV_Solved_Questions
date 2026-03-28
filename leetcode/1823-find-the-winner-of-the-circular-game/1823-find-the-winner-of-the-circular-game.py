class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([i for i in range(1, n + 1)])

        def play(count, index):
            nonlocal queue
            if len(queue) == 1:
                return

            num = queue.popleft()

            if count == k:
                play(1, index + 1)
            else:
                count += 1
                queue.append(num)
                play(count, index + 1)
        
        play(1, 0)
        return queue[0]