import collections

def main(edges):
    graph = collections.defaultdict(list)
    nodeCount = collections.defaultdict(int)
    distance = collections.defaultdict(int)

    for s, v in edges:
        graph[s].append(v)
        graph[v].append(s)

    def getCount(node, parent):
        nodeCount[node] = 1
        for nei in graph[node]:
            if node == parent:
                continue
            getCount(nei, node)
            nodeCount[node] += nodeCount[nei]
            distance[node] = distance[nei] + nodeCount[nei]

    def getMinDistance(node, parent):
        if parent != -1:
            distance[node] = distance[parent] + (nodeCount[0] - nodeCount[node]) - (nodeCount[node])

        for nei in graph[node]:
            if nei == parent:
                continue
            getMinDistance(nei, node)


    getCount(0, -1)
    getMinDistance(0, -1)

    return distance
