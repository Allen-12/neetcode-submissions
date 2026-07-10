class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < 1 or len(t) < 1:
            return False

        s_dict = dict()
        t_dict = dict()

        for character in s:
            if character in s_dict:
                s_dict[character] += 1
            else:
                s_dict[character] = 1
        
        for character in t:
            if character in t_dict:
                t_dict[character] += 1
            else:
                t_dict[character] = 1
        
        character_difference = list(set(s_dict.keys()) - set(t_dict.keys())) + list(set(t_dict.keys()) - set(s_dict.keys()))
        if(len(character_difference) > 0):
            return False
        else:
            for character in s_dict:
                if s_dict[character] != t_dict[character]:
                    return False

        return True
