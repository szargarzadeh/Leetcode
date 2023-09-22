class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_t, idx_s = 0, 0
        res = ""
        while idx_t < len(t) and idx_s < len(s):
            if t[idx_t] == s[idx_s]:
                res += s[idx_s]
                idx_s += 1
            idx_t += 1

        if res == s:
            return True

        return False

