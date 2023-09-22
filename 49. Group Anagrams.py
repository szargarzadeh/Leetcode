from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = defaultdict(lambda: [])
        for st in strs:
            map_dict[''.join(sorted(st))].append(st)

        return list(map_dict.values())



