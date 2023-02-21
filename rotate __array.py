class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # TC:O(N) & SC:O(1)
        k %= len(nums)
        
        ptr1 = 0
        ptr2 = k - 1

        N = len(nums)
        
        def reverse_array(ptr1 , ptr2):
            while ptr1 < ptr2 :
                nums[ptr1] , nums[ptr2] = nums[ptr2] , nums[ptr1]
                ptr1 += 1
                ptr2 -= 1
        
        
        reverse_array(0,N-1)
        reverse_array(0,k-1)
        reverse_array(k,N-1)
