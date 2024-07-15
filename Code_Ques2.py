  # 75. Sort Colors
  # Medium
  
  # Topics
  # Companies
  
  # Hint
  # Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
  
  # We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
  
  # You must solve this problem without using the library's sort function.



# Solution:

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = [0,1,2]
        length = len(nums)
        final = 0 - length - 1
        print(final)
        final_arr =[0] * length
        count_arr = []
        
        for i in k:
            count_arr.append(nums.count(i))

        for i in range(1, len(count_arr)):
            count_arr[i] = count_arr[i] + count_arr[i - 1]

        for i in range(-1, -len(nums) - 1, -1):
            final_arr[count_arr[nums[i]] - 1] = nums[i]
            count_arr[nums[i]] -= 1
            # print(final_arr)

        for i in range(len(nums)):
            nums[i] = final_arr[i]




            

        
                

        
