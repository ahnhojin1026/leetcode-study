class Solution:
    def hammingWeight(self, n: int) -> int:

        mask1 = 0x55555555 # 01010101...
        mask2 = 0x33333333 # 00110011...
        mask3 = 0x0f0f0f0f # 00001111...
        mask4 = 0x00ff00ff # 0000000011111111...
        mask5 = 0x0000ffff # 00000000000000001111111111111111

        n = (n & mask1) + ((n >> 1) & mask1)
        n = (n & mask2) + ((n >> 2) & mask2)
        n = (n & mask3) + ((n >> 4) & mask3)
        n = (n & mask4) + ((n >> 8) & mask4)
        n = (n & mask5) + ((n >> 16) & mask5)

        return n
        