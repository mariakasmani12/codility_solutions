# PROBLEM STATEMENT:
# There are N people sitting at a round table, having dinner. They are numbered from 0 to N-1 in clockwise order. Initially,
# each person has a dish on the table in front of them. Person number K does not like the taste of A[K], but has a dish of taste B[K]. 
# We want every person to have a dish of a taste that they do not dislike, i.e. A[K] ≠ B[K] for each K from 0 to N-1.

# In order to achieve this, you can rotate the whole table clockwise by one position any number of times.
# Rotating the table corresponds to moving the last element of B to the beginning. For example, given A = [3, 6, 4, 5] and B = [2, 6, 3, 5], 
# if we rotate the table once, we would obtain B = [5, 2, 6, 3].

# Find the minimum number of table rotations that need to be performed in order to satisfy every person.

# LINK 
# https://app.codility.com/c/run/trainingC3UVW6-F2D/


def solution(A, B):
    N = len(A)
    
    for r in range(N):
        valid = True
        for i in range(N):
            
            if A[i] == B[(i - r) % N]:
                valid = False
                break
        if valid:
            return r  
    return -1