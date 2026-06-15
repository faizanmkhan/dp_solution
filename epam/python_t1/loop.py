def factorial():
    n = int(input())
    result = 1
    if (n < 0):
        print ("input is negative")
        return
    if (n >= 0):
        for i in range(1, n+1):
            result = result*i
        print (result)

factorial()
