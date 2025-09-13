# 3sum (threeSum) Solution
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res



#a sample test case
if __name__ == "__main__": #this block will only run if the script is executed directly
    solution = Solution() #create an instance of the Solution class
    nums = [-1, 0, 1, 2, -1, -4] #example input list
    result = solution.threeSum(nums) #call the threeSum method
    print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]
