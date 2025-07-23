# PROBLEM STATEMENT:
# 
# A block is a word consisting of one type of letter. For example, aaaa and xx are blocks 
# and bbbcc (two different letters) and xyz (three different letters) are not.
# A string S consisting of N small letters from the English alphabet is given.
# We want to delete as few letters as possible from S to obtain a word composed of at most three blocks.

# LINK
# https://app.codility.com/c/run/trainingBWZQ9Y-99Y/

from collections import defaultdict
def solution(S):
    

    N = len(S)
    max_len = 0

    
    alphabet = set(S)
    letters = list(alphabet)

    for i in range(len(letters)):
        for j in range(len(letters)):
            for k in range(len(letters)):
                used = [letters[i]]
                if letters[j] != letters[i]:
                    used.append(letters[j])
                if letters[k] != letters[j] and letters[k] != letters[i]:
                    used.append(letters[k])

                curr_len = 0
                blocks = []
                prev = ''
                for ch in S:
                    if ch not in used:
                        continue
                    if ch != prev:
                        if len(blocks) == 3:
                            break
                        blocks.append(ch)
                    curr_len += 1
                    prev = ch

                max_len = max(max_len, curr_len)

    return max_len
