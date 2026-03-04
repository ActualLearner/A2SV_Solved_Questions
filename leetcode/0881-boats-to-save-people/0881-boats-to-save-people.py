class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people.sort()

        left, right = 0, N - 1
        pairs = 0

        while left < right:
            sum_ = people[left] + people[right]
            if sum_ <= limit:
                pairs += 1
                left += 1
                right -= 1
            else:
                right -= 1

        return pairs + (N - 2*pairs)