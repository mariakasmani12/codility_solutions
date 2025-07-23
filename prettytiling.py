# problem statement:
# 
# Tom is decorating the pavement in his garden with N square tiles. Each tile is divided into four triangles of different colors 
# (white - 'W', red - 'R', green - 'G' and blue - 'B'). A tile is described as a string of four characters denoting respectively,
# the color of the upper, right, bottom and left triangle. 
# For example, the tile in the figure below is described as "WRGB".
# LINK
# https://app.codility.com/c/run/trainingF77RFU-MMM/



def rotate(tile):
    return tile[3] + tile[0] + tile[1] + tile[2]

def rotation_cost(r):
    return min(r, 4 - r)

def solution(A):
    N = len(A)

    rotations = []
    for tile in A:
        tile_rot = [tile]
        for _ in range(3):
            tile_rot.append(rotate(tile_rot[-1]))
        rotations.append(tile_rot)


    dp = [[float('inf')] * 4 for _ in range(N)]

    for r in range(4):
        dp[0][r] = rotation_cost(r)

    for i in range(1, N):
        for r in range(4):
            for prev_r in range(4):  
                if rotations[i-1][prev_r][1] == rotations[i][r][3]: 
                    dp[i][r] = min(dp[i][r], dp[i-1][prev_r] + rotation_cost(r))

    return min(dp[N-1])
