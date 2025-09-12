# 3sum (threeSum) Solution
class Solution(object):
    def threeSum(self, nums):
        res = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tri = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(tri)
        return list(res)



#a sample test case
if __name__ == "__main__": #this block will only run if the script is executed directly
    solution = Solution() #create an instance of the Solution class
    nums = [-1, 0, 1, 2, -1, -4] #example input list
    result = solution.threeSum(nums) #call the threeSum method
    print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]
