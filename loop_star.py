def loop (n):
    '''for i in range (5,0,-1): # half pyramid printing 
        print('*'*i) '''

    
    '''for i in range(1,n): # pyramid printing how many times should print
        print("  "*(n-i),end=" ") # printing spaces
        for k in range(1,2*i):
    # printing * , 1 to 2*i because at least one time should always run
            print('*',end=" ")
        print('\n')'''

    for i in range(n,0,-1):
        print("  "*(n-i),end = " ")
        for j in range(2*i-1):
            print("*",end = " ")
        print('\n')
a = loop(5)
