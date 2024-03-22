class Solution:
    def mergeSortedArray(self, nums1, m, nums2, n):
        p = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1

        while j >= 0:
            nums1[p] = nums2[j]
            p -= 1
            j -= 1
