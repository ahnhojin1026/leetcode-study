class Solution:
    def climbStairs(self, n: int) -> int:
        # Base Cases
        if n == 1:
            return 1
        elif n==2 :
            return 2
        # Opminization: Using rolling array to reduce space complexity
        dp = [0,0,0]

        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            # Slide the window
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[0] + dp[1]

        return dp[2]