class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        left, right = 0, len(A) - 1
        while True:
            mid = (left + right) // 2
            idx = half - mid - 2

            Aleft = A[mid] if mid >= 0 else float("-inf")
            Aright = A[mid+1] if (mid + 1) < len(A) else float("inf")
            Bleft = B[idx] if idx >= 0 else float("-inf")
            Bright = B[idx + 1] if (idx + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    val1 = max(Aleft, Bleft)
                    val2 = min(Aright, Bright)
                    return (val1 + val2) / 2

            elif Aleft > Bright:
                right = mid - 1
            else:
                left = mid + 1

