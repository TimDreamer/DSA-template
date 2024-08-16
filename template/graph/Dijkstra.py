import collections
import math
import heapq

def main(n, edges, source, target):
    graph = collections.defaultdict(list)

    for s, v, w in edges:
        graph[s].append((v, w))
        graph[v].append((s, w))

    queue = [(0, source)]
    distance = [math.inf] * n
    distance[source] = 0

    while queue:
        dst, node, w = heapq.heappop(queue)

        if distance[node] < dst:
            continue

        if node == target:
            return dst

        for nei in graph[node]:
            if distance[nei] > dst + w:
                distance[nei] = dst + w
                heapq.heappush(queue, (distance[nei], nei))

    return -1
