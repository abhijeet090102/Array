def minimum():
    nums = [2,11,10,1,3]
    
    '''arr = []
    alice = 0
    bob = 0
##    if nums is not None:
    for i in range(len(nums)//2):
        alice = min(nums)
        nums.remove(alice)
        bob = min(nums)
        nums.remove(bob)
        arr.append(bob)
        arr.append(alice)'''

    '''nums.sort()
    for i in range(0,len(nums),2):
        nums[i] ,nums[i+1] = nums[i+1] , nums[i]
    print(nums)'''
    nums.sort()
    count = 0
    
    k = 10
    for i in nums:
        if i < k:
            count += 1
        
    print(count)
    
am = minimum()
