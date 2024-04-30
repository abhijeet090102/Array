''' Truncate Sentence '''
class Solution:
    def truncSentence(self, s: str, k: int) -> str:
        lst = [] 
        st = s.split(" ")
        for i in range(len(st)):
            if i == k:
                break
            else:
                lst.append(st[i])
        
        return ' '.join(lst)

        '''return " ".join(s.split(" ")[:k])
            # both work perfectly fine
            '''
am = Solution()
t = "Hello how are you Coder friend"
k = 5
print(am.truncSentence(t,k))
