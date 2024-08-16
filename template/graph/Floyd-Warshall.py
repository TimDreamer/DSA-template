import math

def main(n, edges, source, target):
    distance = [[math.inf] * n for _ in range(n)]

    for i in range(n):
        distance[i][i] = 0

    for s, v, w in edges:
        distance[s][v] = distance[v][s] = w

    for k in range(N):
        for i in range(N):
            for j in range(N):
                distance[i][j] = min(distance[i][k], distance[i][k] + distance[k][j])

    return distance[source][target]
