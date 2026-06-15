def intsum():
    n = input()
    cn = int(n)
    result = 0
    if (cn < 0):
        print ("input is negative")
        return
    for ch in n:
        result = result + int(ch)
    print (result)

intsum()