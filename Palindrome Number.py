#Solution
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        realNum = x
        res,rem =0,0
        while x!=0:
            rem = x%10
            res = res*10 +rem
            x = x//10
        return realNum == res



#a sample test case
if __name__ == "__main__": #main block
    solution = Solution() #create an object of the Solution class
    x = 121 #example input number
    result = solution.isPalindrome(x) #call the isPalindrome method
    print(result)  # Output: True
