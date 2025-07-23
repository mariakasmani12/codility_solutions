#PROBLEM STATEMENT:
#  You analyze the performance of a computer network. The network comprises nodes connected by peer-to-peer links.
# There are N links and N + 1 nodes. All pairs of nodes are (directly or indirectly) connected by links, and
# links don't form cycles. In other words, the network has a tree topology.

# Your analysis shows that communication between two nodes performs much better if the number of links on the 
# (shortest) route between the nodes is odd. Of course, the communication is fastest when the two nodes are connected by a direct link. But,
# amazingly, if the nodes communicate via 3, 5, 7, etc. links, communication is much faster than if the number of links to pass is even.

# Now you wonder how this influences the overall network performance. There are N * (N + 1) / 2 different pairs of nodes. 
# You need to compute how many of them are pairs of nodes connected via an odd number of links.

# Nodes are numbered from 0 to N. Links are described by two arrays of integers, A and B, each containing N integers.
# For each 0 ≤ I < N, there is a link between nodes A[I] and B[I].

# LINK
# https://app.codility.com/c/run/trainingKT3D6E-UDC/

from collections import defaultdict, deque

def solution(A, B):
    N = len(A)
    graph = defaultdict(list)

   
    for u, v in zip(A, B):
        graph[u].append(v)
        graph[v].append(u)

   
    visited = [False] * (N + 1)
    depth = [0] * (N + 1)
    even_count = 0
    odd_count = 0

    queue = deque()
    queue.append(0)
    visited[0] = True

    while queue:
        node = queue.popleft()
        if depth[node] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1
                queue.append(neighbor)

  
    return even_count * odd_count