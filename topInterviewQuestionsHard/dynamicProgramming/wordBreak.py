from imports import *

"""
A very classic LeetCode problem...
This page helped us a lot in understanding the three different methods (DFS, BFS, DP):
https://helloacm.com/cc-coding-exercise-word-break-dp-bfs-dfs/
"""

class Solution1:
    """
    Simple iterative BFS or DFS.
    https://leetcode.com/problems/word-break/discuss/428606/Python-Simple-Iterative-BFS-or-DFS-24ms
    Failed (Time Limit Exceeded) for the below test case:
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque()
        q.append(s)
        seen = set() 
        while len(q):
            s = q.popleft() # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    q.append(new_s)
                    if new_s not in seen:
                       q.append(new_s)
                       seen.add(new_s)
        return False
        

if __name__ == "__main__":
    print(Solution1().wordBreak(
        "aaab",
        ["a","aa"]))