class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in range(len(strs)):
            # Sort the string to form the key
            key = "".join(sorted(strs[i]))
            
            # append the string to the corresponding key in the dictionary
            if key in ans:
                ans[key].append(str(strs[i]))
            else:
                ans[key] = [str(strs[i])]
                
        # print(ans)
        # values() method returns a view object that displays a list of all the values in the dictionary.
        return list(ans.values())