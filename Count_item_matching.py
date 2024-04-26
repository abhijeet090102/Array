''' count item matching a rule '''
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str):
        count = 0
        '''for i in items:
            if ruleKey == "type" and i[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and i[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and i[2] == ruleValue:
                count += 1'''
        
        if ruleKey == "type":
            for i in items:
                if i[0] == ruleValue:
                    count +=1
        if ruleKey == "color":
            for i in items:
                if i[1] == ruleValue:
                    count +=1
        if ruleKey == "name":
            for i in items:
                if i[2] == ruleValue:
                    count +=1
        return count
am = Solution()
lst = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = 'color'
ruleValue = 'silver'
print(am.countMatches(lst,ruleKey,ruleValue))
