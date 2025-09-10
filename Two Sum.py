#Solution
class Solution:
    def twoSum(self, my_list, target):
        for i in range(len(my_list)):
            for j in range(i+1,len(my_list)):
                if my_list[i] + my_list[j] == target:
                    return [i,j]



#a sample test case
if __name__ == "__main__": #this block will only run if the script is executed directly
    solution = Solution() #create an instance of the Solution class
    my_list = [2, 7, 11, 15] #example input list
    target = 9 #example target sum
    result = solution.twoSum(my_list, target) #call the twoSum method
    print(result)  # Output: [0, 1]
