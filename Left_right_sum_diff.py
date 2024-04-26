''' left and right sum differences '''
class Solution:
    def leftRightDiff(self, nums: list[int]) :
        rightSum = [0]*len(nums) 
        leftSum = [0]*len(nums)
        leftSum[0] = nums[0]
        
        for i in range(1,len(nums)):
            # for calculating left sides sum of the elements to the index i 
            leftSum[i] = leftSum[i-1] + nums[i]
            
# assigning the lat index value first for calculating others sums
        rightSum[len(nums)-1] = nums[len(nums)-1]
        #negetive direction travarsign for right sum 
        for j in range(len(nums)-2,-1,-1):
            # calculating the sum of the element to the right of the index j 
            rightSum[j] = rightSum[j+1] + nums[j]

        # now calculating the sum differences and storing into a new array 
        answer = [0]*len(nums)
        for i in range(len(nums)):
            answer[i] = abs(leftSum[i] - rightSum[i])
        return answer

am = Solution()
lst = [10,4,8,6,2,7]
print(am.leftRightDiff(lst))
