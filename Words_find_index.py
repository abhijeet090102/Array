''' Find Words Containing Character '''
class Solution:
    def findWordsConta(self, words: list[str], x: str):
        result = []
        '''for i,wo in enumerate(words):
            if x in wo:
                result.append(i)
        return result'''
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        return result
am = Solution()
lst = ['abhij','mani','annap']
x = 'a'
print(am.findWordsConta(lst,x))
