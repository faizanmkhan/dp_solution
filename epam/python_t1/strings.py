def palindrome():
    input_str = input()
    reverse_str = input_str[::-1]
    if input_str == reverse_str:
        print("yes")
    else:
        print("no")
    return

palindrome()
