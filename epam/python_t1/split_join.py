def reverse_words():
    string = input()
    words = string.split()

    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    print(" ".join(reversed_words))

reverse_words()