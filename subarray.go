func solution(a []int) int {
    n := len(a)
    l := make([]int, n)
    r := make([]int, n)
    for i := 0; i < n; i++ {
        l[i], r[i] = 1, 1
    }
    for i := 1; i < n; i++ {
        if a[i] > a[i-1] {
            l[i] = l[i-1] + 1
        }
    }
    for i := n - 2; i >= 0; i-- {
        if a[i] < a[i+1] {
            r[i] = r[i+1] + 1
        }
    }
    ans := 1
    for _, x := range l {
        if x > ans {
            ans = x
        }
    }
    if n > 1 {
        if r[1]+1 > ans {
            ans = r[1] + 1
        }
        if l[n-2]+1 > ans {
            ans = l[n-2] + 1
        }
    }
    for i := 1; i+1 < n; i++ {
        if a[i-1] < a[i+1] && l[i-1]+r[i+1]+1 > ans {
            ans = l[i-1] + r[i+1] + 1
        }
    }
    return ans
}