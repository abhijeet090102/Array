''' How many Numbers are smaller than the current number '''
class Solution:
    def smaNumTHCurrents(self, nums: list[int]):
        
        st = []
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if j != i and nums[j] < nums[i]:
                    count +=1
            st.append(count)
        return st

am = Solution()
lst  = [6,5,8,9,2,3,4]
print(am.smaNumTHCurrents(lst))
