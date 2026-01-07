class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-up DP
        dp = [-1] * (amount + 1)
        # Base case
        dp[0] = 0

        # Fill the dp array
        for i in range(1, amount + 1):
            # Try every coin
            for c in coins:
                # if the coin can contribute to the amount i
                if i - c >= 0 and dp[i-c] != -1:
                    # Update dp[i]
                    if dp[i] == -1:
                        dp[i] = dp[i-c] + 1
                    else:
                        dp[i] = min(dp[i-c] + 1, dp[i])
                    

        return dp[amount]