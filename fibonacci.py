def fib_dp(n):
    if n <= 1:
        return n

    prev2, prev1 = 0, 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print(f"Fibonacci({n}) [bottom-up]  = {fib_dp(n)}")
    print(f"Fibonacci({n}) [memoized]   = {fib_memo(n)}")