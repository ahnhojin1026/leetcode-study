class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (m+n-2) C (n-1)
        # Ensure n is the smaller one
        if m < n:
            swap = n
            n = m
            m = swap
        # now n is always same or smaller than m

        # calculate factorial and multiplication
        n_fac = 1
        m_mul = 1
        for i in range(1,n):
            n_fac *= i
            m_mul *= (n+m-1 - i)

        return m_mul // n_fac 