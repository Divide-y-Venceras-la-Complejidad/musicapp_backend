import heapq
import numpy as np

def bfs_first_height_max_heap(G, s):
    n = len(G)
    visited = [False] * n
    path = [-1] * n  # parent
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)
        if path[u] != -1:
            # Already visited a vertex at the first height
            continue
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                path[v] = u
                queue.append(v)

    max_heap = []
    for vertex, parent in enumerate(path):
        if parent == s:
            heapq.heappush(max_heap, (-G[s][vertex], vertex))

    return [heapq.heappop(max_heap)[1] for _ in range(min(10, len(max_heap)))]
 

def executeMusicAlgorithm(music_id, filter_type):
    
    matrix = []
    G = []
    if filter_type == 'genre':
        G = np.loadtxt("archives/genreMatrix.txt")
    elif filter_type == 'artist':
        G = np.loadtxt("archives/artistMatrix.txt")
    elif filter_type == 'topic':
        G = np.loadtxt("archives/topicMatrix.txt")
    else: 
        G = np.loadtxt("archives/yearMatrix.txt")

    relatedMusicsId = bfs_first_height_max_heap(G, music_id)

    return relatedMusicsId