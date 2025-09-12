#Solution
class Solution(object):
    def lengthOfLastWord(self, s):
        lst = s.split()
        return len(lst[-1]) if lst else 0


# a sample test case
if (
    __name__ == "__main__"
):  # this block will only run if the script is executed directly
    solution = Solution()  # create an instance of the Solution class
    s = "Hello World"  # example input string
    result = solution.lengthOfLastWord(s)  # call the lengthOfLastWord method
    print(result)  # Output: 5
