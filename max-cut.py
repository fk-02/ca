n = int(input())
a, b, c = map(int, input().split())
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for x in (a, b, c):
        if i >= x and dp[i - x] != -1:
            dp[i] = max(dp[i], dp[i - x] + 1)
print(max(0, dp[n]))