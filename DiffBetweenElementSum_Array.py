''' Difference Between Element Sum and Digit Sum of an Array '''
class Solution:
    def differenceOfSum(self, nums: list[int]):
        am = 0
        ts = 0
        for i in nums:
            ts += i
        for i in range(len(nums)):
            while nums[i] > 0:
                am += nums[i] %10
                nums[i] //= 10
        
        return abs(am - ts)
am = Solution()
nu = [1,15,6,3]
print(am.differenceOfSum(nu))
