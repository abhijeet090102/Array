''' Shuffle String '''
class Solution:
    def restoreString(self, s: str, indices: list[int]):
        st = ['']*len(s)
        for i in range(len(s)):
            st[indices[i]] = s[i]
        return ''.join(st)
am = Solution()
st = "maamam"
st = "abhije"
st = "mashani"
ind = [0,1,4,5,6,2,3]
print(am.restoreString(st,ind))
