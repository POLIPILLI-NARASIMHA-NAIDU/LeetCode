#Solution
class Solution(object):
    def plusOne(self, digits):
        num = int(''.join(map(str,digits)))+1
        return [int(d) for d in str(num)]



#a sample test case
if __name__ == "__main__":  # this block will only run if the script    is executed directly
    solution = Solution()  # create an instance of the Solution class
    digits = [1,2,3]  # example input list
    result = solution.plusOne(digits)  # call the plusOne method
    print(result)  # Output: [1, 2, 4]
