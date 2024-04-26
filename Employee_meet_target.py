''' Numbers of employee who meet the target '''
class Solution:
    def NoEmpMetTarget(self, hours: list[int], target: int):
        count = 0
        for i in range(len(hours)):
            if hours[i] < target :
                print(f'Employee {i} worked for {hours[i]} hours and didn"t meet the target .')
            elif hours[i] >= target:
                print(f'Employee {i} worked for {hours[i]} hours and meet the target . ')
                count += 1
        return count
am = Solution()
lst = [5,6,4,2,2,8,1]
ts = 6
print(am.NoEmpMetTarget(lst,ts))
