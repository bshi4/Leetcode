class Solution:
    def twoSum(self, numbers, target):
        error_message = 'No answer'
        dict1 = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dict1:
                return [dict1[target-numbers[i]]+1, i+1]
            dict1[numbers[i]] = i
        return error_message
        