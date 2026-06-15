def list_control():
    lst = []
    n = int(input())
    for _ in range(n):
        parts = input().split()
        cmd = parts[0]

        if cmd == "insert":
            lst.insert(int(parts[1]), int(parts[2]))

        elif cmd == "print":
            print(lst)

        elif cmd == "remove":
            lst.remove(int(parts[1]))

        elif cmd == "append":
            lst.append(int(parts[1]))

        elif cmd == "sort":
            lst.sort()

        elif cmd == "pop":
            lst.pop()

        elif cmd == "reverse":
            lst.reverse()

list_control()