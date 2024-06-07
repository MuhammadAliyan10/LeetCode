class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, n + m - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
       
       
#!The time complexity of this algorithm is O(m + n), where m is the number of valid elements in nums1 and n is the number of elements in nums2.
#!The space complexity of this algorithm is O(1).