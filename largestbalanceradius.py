# PROBLEM STATEMENT:
# 
# There are N points (numbered from 0 to N−1) on a plane. Each point is colored either red ('R') or green ('G'). The K-th point is
#  located at coordinates (X[K], Y[K]) and its color is colors[K]. No point lies on coordinates (0, 0).
# We want to draw a circle centered on coordinates (0, 0), such that the number of red points and 
# green points inside the circle is equal. What is the maximum number of points that can lie inside such a circle? 
# Note that it is always possible to draw a circle with no points inside.

# LINK
#https://app.codility.com/c/run/trainingV99VAE-TVR/

def solution(X, Y, colors):
    N = len(X)
    points = []
    
    for i in range(N):
        dist_sq = X[i] * X[i] + Y[i] * Y[i]
        points.append((dist_sq, colors[i]))

    # Sort by distance from origin
    points.sort()

    red = 0
    green = 0
    max_points = 0

    for i in range(N):
        color = points[i][1]
        if color == 'R':
            red += 1
        else:
            green += 1

        if red == green:
            max_points = max(max_points, red + green)

    return max_points