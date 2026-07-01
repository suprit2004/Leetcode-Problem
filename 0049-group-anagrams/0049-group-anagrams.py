class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        group=defaultdict(list)
        for s in strs:
            key=" ".join(sorted(s))
            group[key].append(s)
        return list(group.values())