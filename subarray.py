from random import randint

def f(a):
	n=len(a)
	l=[1]*n
	r=[1]*n
	for i in range(1,n):l[i]=l[i-1]+1 if a[i]>a[i-1] else 1
	for i in range(n-2,-1,-1):r[i]=r[i+1]+1 if a[i]<a[i+1] else 1
	q=max(l)
	if n>1:q=max(q,r[1]+1,l[-2]+1)
	for i in range(1,n-1):
		if a[i-1]<a[i+1]:q=max(q,l[i-1]+r[i+1]+1)
	return q

tests = [
    ([1], 1),
    ([1, 2], 2),
    ([2, 1], 2),
    ([1, 2, 3, 4], 4),
    ([4, 3, 2, 1], 1),
	([5, 4, 3, 2, 1], 2),
    # classic peak break
    ([1, 2, 100, 3, 4], 5),

    # no improvement possible
    ([1, 3, 2, 4], 3),

    # already increasing
    ([1, 2, 3, 5, 6, 7], 6),

    # tricky case (cannot fully merge)
    ([1, 5, 3, 4, 6], 3),

    # duplicate break
    ([1, 2, 2, 3, 4], 4),

    # zigzag
    ([10, 20, 10, 20, 10], 2),
]

for i, (arr, expected) in enumerate(tests):
    result = f(arr)
    print(f"Test {i+1}: {arr}")
    print(f"Expected: {expected}, Got: {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)


# -------------------------
# RANDOM STRESS TEST (optional)
# -------------------------

def brute(a):
    # brute force: remove one element or none
    n = len(a)
    best = 1

    for skip in range(n + 1):
        arr = a[:skip] + a[skip+1:] if skip < n else a[:]
        # compute longest increasing subarray
        cur = 1
        best_local = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                cur += 1
            else:
                cur = 1
            best_local = max(best_local, cur)
        best = max(best, best_local)

    return best


print("\n--- RANDOM STRESS TEST ---")
for _ in range(1000):
    arr = [randint(1, 20) for _ in range(randint(1, 10))]
    if f(arr) != brute(arr):
        print("Mismatch found!")
        print(arr)
        print("solution:", f(arr))
        print("brute:", brute(arr))
        break
else:
    print("All random tests passed!")