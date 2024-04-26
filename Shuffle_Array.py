''' Shuffle the array '''
class Solution:
    def shuffle(self, nums: list[int], n: int):
        lst = []
        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[i+n])
        return lst
ma = Solution()
lst = [2,5,1,3,4,7]
print(ma.shuffle(lst,3))
