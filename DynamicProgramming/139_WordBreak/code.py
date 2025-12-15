class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # use Set for O(1) search (list has O(n) search time)
        wordDict_set = set(wordDict)
        
        # dp[i] means s[0:i+1] can be segmented into words in wordDict
        dp = [False] * len(s)

        for end_index in range(len(s)):
            # if the whole substring is in wordDict
            if s[:end_index+1] in wordDict_set:
                dp[end_index] = True
            else:
                for mid in range(end_index):
                    # check if the substring is composede of two parts
                    if dp[mid] and s[mid+1:end_index+1] in wordDict_set:
                        dp[end_index] = True
                        break
                    
        # return whether the whole string can be segmented
        return dp[len(s) - 1]