class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = 0, 0

        while idx1 < m + n and idx2 < n:
            if nums2[idx2] > nums1[idx1]:
                idx1 += 1
            else:
                nums1.insert(idx1, nums2[idx2])
                nums1.pop()
                idx2 += 1

        for i in range(len(nums2[idx2:])):
            nums1.pop()

        nums1.extend(nums2[idx2:])





