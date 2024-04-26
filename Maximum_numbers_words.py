'''Maximum Number of words found in sentences '''
class Solution:
    def mostWordsFound(self, sentences: list[str]):
        count = 0
        wd = ''
        for i in sentences:
            word = len(i.split(" "))
            if word > count :
                count = word
                wd = i
        print(wd)
        return count
ma = Solution()
lst = ['i am posting my codes' , 'for your better understanding' , 'to build knowledge of coding worlds']
print(ma.mostWordsFound(lst))
