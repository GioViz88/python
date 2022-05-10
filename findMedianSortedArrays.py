class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = (nums1+nums2)
        new_arr.sort()
        if len(new_arr) %2==0:
            first_index = int(len(new_arr)/2)
            second_index = int(first_index-1)

            median = (new_arr[first_index]+new_arr[second_index])/2
            return median
        else:
            index = int((len(new_arr)-1)/2)
            median = new_arr[index]
            return median
