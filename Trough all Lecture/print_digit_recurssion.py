def printdig(n):
    if n/10 == 0:
        return
    
    print(n%10) # print the last digit first
    printdig(n//10)
    # print(n%10) # print the 1st digit first

printdig(12345)