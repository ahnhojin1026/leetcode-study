class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            # push ans to left by 1 to make space for next bit
            ans = (ans << 1) 
            
            # append LSB of n to ans
            if n & 1:
                ans |= 1
            
            # push n to right by 1 to process next bit
            n >>= 1
            
        return ans