import re
from itertools import permutations

def pattern_to_regex(s):
    return "^" + s.replace("*", ".") + "$"

def solution(user_id, banned_id):
    answer = 0
    res = set()
    
    for perm in permutations(user_id, len(banned_id)):
        valid = True

        for p, b in zip(perm, banned_id):
            regex = pattern_to_regex(b)
            if not re.fullmatch(regex, p):
                valid = False
                break
            
        if valid:
            res.add(frozenset(perm))
    
    answer = len(res)
    return answer