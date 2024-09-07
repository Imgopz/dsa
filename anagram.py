class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):

            print(s[i], t[i])
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

            print(countS.get(s[i]), countT.get(t[i]))
        return countS == countT


sol = Solution()

res = sol.isAnagram(s="anagram", t="nagaram")

print(res)

# Python implements hashmaps through the built-in dictionary data type. Like hashmaps, dictionaries store data in {key:value} pairs. Once you create the dictionary (see the next section), Python will apply a convenient hash function under the hood to calculate the hash of every key.