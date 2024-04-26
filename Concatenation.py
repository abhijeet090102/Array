''' concatenation of array '''
class Solution:
    def getConcatenation(self, nums: list[int]):
        ans = []
        for i in range(0,2*len(nums)):
            ans.append(nums[i%len(nums)])
        return ans
am = Solution()
lst = [1,3,2,1]
print(am.getConcatenation(lst))
