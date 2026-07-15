class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [(string, "".join(sorted(string))) for string in strs]
        group_map = dict()

        for tuple_str in sorted_strs:
            if tuple_str[1] in group_map:
                group_map[tuple_str[1]].append(tuple_str[0])
            else:
                group_map[tuple_str[1]] = [tuple_str[0]]
        
        return list(group_map.values())