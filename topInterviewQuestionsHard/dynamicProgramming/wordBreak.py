from imports import *

"""
A very classic LeetCode problem...
This page helped us a lot in understanding the three different methods (DFS, BFS, DP):
https://helloacm.com/cc-coding-exercise-word-break-dp-bfs-dfs/
"""

class Solution:
    """
    Runtime: 36 ms, faster than 87.39% of Python3 online submissions for Word Break.
    Memory Usage: 14.5 MB, less than 47.15% of Python3 online submissions for Word Break.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        https://leetcode.com/problems/word-break/discuss/748479/Python3-Solution-with-a-Detailed-Explanation-Word-Break
        For similar questions DP is generally a not-too-bad option.
        If dp[i] == True, substring s[0:i] can be segmented.
        Sub-problem:
            * Can a string be splitted into 2 substrings that can be segmented as well.
        Notes:
            * The answer for the first substring is stored in dp[i] already, so only need to check if the second string is in wordDict.
            * One of the substring can be "" meaning the other is the substring itself. 
              For this reason we need to create an array of len(s)+1.
              dp[0] should be set to True for checking if the substring itself is in wordDict.
        Recurrence formula:
            * dp[i] = dp[j] and s[j:i] in wordDict, 0 =< j < i
        When dp[i] is True the inner for loop can terminate earlier.
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

    def bfsWithMemoization(self, s: str, wordDict: List[str]) -> bool:
        """
        https://leetcode.com/problems/word-break/discuss/428606/Python-Simple-Iterative-BFS-or-DFS-24ms
        Simple iterative BFS or DFS with memoization.
        """
        q = deque()
        q.append(s)
        seen = set() 
        while len(q):
            s = q.popleft() # popleft() = BFS; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                       q.append(new_s)
                       seen.add(new_s)
        return False

    """
    Brute force solution would fail (Time Limit Exceeded) the below test case:
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"] 
    """
    def bruteForceIterative(self, s: str, wordDict: List[str]) -> bool:
        """
        n: len(s)
        m: len(wordDict)
        Time complexity: O(2^n*m) because:
            T(n) = T(n-1)+T(n-2)+...+T(1)
            => T(n+1) = T(n)+T(n-1)+T(n-2)+...+T(1)
            => T(n+1) = 2T(n)
        """
        q = deque()
        q.append(s)
        while len(q):
            s = q.pop()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    q.append(new_s)
        return False
    
    def bruteForceRecursive(self, s: str, wordDict: List[str]) -> bool:
        def canBreak(s):
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "":
                        return True
                    if canBreak(new_s):
                        return True
            return False
        return canBreak(s)

if __name__ == "__main__":
    print(Solution().wordBreak(
        "LeetCode",
        ["Leet","Code"]))