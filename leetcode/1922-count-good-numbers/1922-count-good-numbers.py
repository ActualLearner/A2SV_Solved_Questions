class Solution:
    def countGoodNumbers(self, n: int) -> int:
        E = -(-n // 2)
        O = n // 2
        modulo = 10**9 + 7
        return (pow(5, E, modulo) * pow(4, O, modulo)) % modulo