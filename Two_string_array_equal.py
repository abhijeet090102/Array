''' check if two string array are equivalent '''
class Solution:
    def arrStrEqual(self, word1: list[str], word2: list[str]):
        string1 = ''
        string2 = ''
        for i in word1:
            string1 += str(i) # for adding two index string creating a string 
        for j in word2:
            string2 += str(j) # for addign two index string and creating a string 
        return (string1 == string2) # comparing and returning the true or false only 

ma = Solution()
lst1 = ['a','bc']
lst2 = ['ab','c']
print(ma.arrStrEqual(lst1,lst2))
