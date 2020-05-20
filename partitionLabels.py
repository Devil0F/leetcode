class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {s:x for x,s in enumerate(S)}
        first = end = 0
        ans = []
        for i,ss in enumerate(S):
            end = max(end,last[ss])
            if i == end:
                ans.append(i-first+1)
                first = i + 1
        return ans
