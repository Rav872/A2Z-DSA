"""
Description: Connect n ropes with minimal cost
"""
import random
def rod_cutting(prices):
    N = len(prices)
    # Create a table to store the maximum value that can be obtained for each length
    dp = [0] * (N + 1)

    # Build the table dp[] in a bottom-up manner
    for i in range(1, N + 1):
        max_value = 0
        for j in range(1, i + 1):
            max_value = max(max_value, prices[j - 1] + dp[i - j])
        dp[i] = max_value

    return dp[N]

def main():
    
    # prices = [1,5,8,9,10,17,17,20]
    # N = 8
    prices = [random.randint(1, 100) for _ in range(12000)]
    prices.sort()

    print(rod_cutting(prices))
    pass

if __name__ == "__main__":
    main()