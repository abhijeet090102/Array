''' Richest Customer Wealth '''
class Solution:
    def maximumWealth(self, accounts: list[list[int]]):
        result = 0
        '''l = []
        for i in accounts:
            re = 0
            for j in i:
                re += j
            l.append(re)
        return max(l)'''
                
        for i in range(len(accounts)):
            total = sum(accounts[i]) 
            result = max(result,total)
        return result

am = Solution()
acts = [[1,2,3],[3,2,1]]
print(am.maximumWealth(acts))
