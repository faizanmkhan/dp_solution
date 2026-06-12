#include <vector>
#include <algorithm>

int solution(std::vector<int>& a)
{
    int n = a.size(), ans = 1;
    std::vector<int> l(n, 1), r(n, 1);
    for (int i = 1; i < n; i++) l[i] = a[i] > a[i - 1] ? l[i - 1] + 1 : 1;
    for (int i = n - 2; i >= 0; i--) r[i] = a[i] < a[i + 1] ? r[i + 1] + 1 : 1;
    for (int x : l) ans = std::max(ans, x);
    if (n > 1) ans = std::max(ans, std::max(r[1] + 1, l[n - 2] + 1));
    for (int i = 1; i + 1 < n; i++)
        if (a[i - 1] < a[i + 1]) ans = std::max(ans, l[i - 1] + r[i + 1] + 1);
    return ans;
}
