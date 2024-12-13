"""
Lab 2
"""

def read_incidence_matrix(filename: str) -> list[list]:
    """
    A function that takes in a name of file, returns a list of lists,
    which show the rows of a digraph incidence matrix

    :param str filename: The name of the file 
    :returns list[list]: the incidence matrix of a given graph

    >>> import tempfile
    >>> import os
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(\
    "digraph sample_input {\\n\
    0 -> 1;\\n\
    0 -> 2;\\n\
    1 -> 0;\\n\
    1 -> 2;\\n\
    2 -> 0;\\n\
    2 -> 1;\\n\
    }"\
    )
    ...     tmp_path = tmp.name
    >>> read_incidence_matrix(tmp_path)
    [[-1, -1, 1, 0, 1, 0], [1, 0, -1, -1, 0, 1], [0, 1, 0, 1, -1, -1]]
    >>> os.remove(tmp_path)
    """

    with open(filename, 'r', encoding='utf-8') as f:
        edges = [tuple(map(int, line.replace(';', '').split('->'))) for line in f if '->' in line]

    vertices = sorted({v for edge in edges for v in edge})

    vertex_indices = {v: i for i, v in enumerate(vertices)}
    incidence_matrix = [[0] * len(edges) for _ in vertices]

    for edge_index, (u, v) in enumerate(edges):
        if u == v:
            # loop
            incidence_matrix[vertex_indices[u]][edge_index] = 2
        else:
            # out
            incidence_matrix[vertex_indices[u]][edge_index] = -1
            # in
            incidence_matrix[vertex_indices[v]][edge_index] = 1

    return incidence_matrix

def read_adjacency_matrix(filename: str) -> list[list]:
    """
    Makes an adjacency graph into a list of lists, where they represent
    rows,

    :param str filename: The name of the file 
    :returns list[list]: the adjacency matrix of a given graph

    
    >>> import tempfile
    >>> import os
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(\
    "digraph sample_input {\\n\
    0 -> 1;\\n\
    0 -> 2;\\n\
    1 -> 0;\\n\
    1 -> 2;\\n\
    2 -> 0;\\n\
    2 -> 1;\\n\
    }"\
    )
    ...     tmp_path = tmp.name
    >>> read_adjacency_matrix(tmp_path)
    [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    >>> os.remove(tmp_path)
    """
    with open(filename, 'r', encoding='utf-8') as f:
        edges = [tuple(map(int, line.replace(';', '').split('->'))) for line in f if '->' in line]

    vertices = sorted({v for edge in edges for v in edge})
    n = len(vertices)
    adjacency_matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        adjacency_matrix[u][v] = 1

    return adjacency_matrix

def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    Makes a dictionary as a simple adjacency dictinoary, where the key is a vertice,
    and the values are the edges that the vertice is connected to

    :param str filename: The name of the file
    :returns dict: Adjacency dictionary of a given graph

    >>> import tempfile
    >>> import os
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(\
    "digraph sample_input {\\n\
    0 -> 1;\\n\
    0 -> 2;\\n\
    1 -> 0;\\n\
    1 -> 2;\\n\
    2 -> 0;\\n\
    2 -> 1;\\n\
    }"\
    )
    ...     tmp_path = tmp.name
    >>> read_adjacency_dict(tmp_path)
    {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    >>> os.remove(tmp_path)
    
    """
    with open(filename, 'r', encoding='utf-8') as f:
        edges = [tuple(map(int, line.replace(';', '').split('->'))) for line in f if '->' in line]

    adjacency_dict = {}
    for u, v in edges:
        adjacency_dict.setdefault(u, []).append(v)

    return adjacency_dict


def iterative_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        traversal.append(current)

        for neighbor in sorted(graph[current], reverse=True):
            if neighbor not in visited:
                stack.append(neighbor)

    return traversal


def iterative_adjacency_matrix_dfs(graph: list[list], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        traversal.append(current)

        for neighbor, connected in list(enumerate(graph[current]))[::-1]:
            if connected and neighbor not in visited:
                stack.append(neighbor)

    return traversal


def recursive_adjacency_dict_dfs(graph: dict[int, list[int]], start: int, path=None) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    if not path:
        path = []

    if start not in path:
        path.append(start)

    for neighbor in sorted(graph[start]):
        if neighbor not in path:
            recursive_adjacency_dict_dfs(graph, neighbor, path)

    return path

def recursive_adjacency_matrix_dfs(graph: list[list[int]], start: int, path=None) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    if not path:
        path = []

    if start not in path:
        path.append(start)

    for neighbor, connected in enumerate(graph[start]):
        if connected and neighbor not in path:
            recursive_adjacency_matrix_dfs(graph, neighbor, path)

    return path

def iterative_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    visited = [False] * len(graph)
    queue = []
    visited[start] = True
    queue.append(start)
    res = []
    while queue:
        ind_v = queue.pop(0)
        res.append(ind_v)
        for ind in graph[ind_v]:
            if not visited[ind]:
                visited[ind] = True
                queue.append(ind)
    return res

def iterative_adjacency_matrix_bfs(graph: list[list[int]], start: int) -> list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    visited = [False] * len(graph)
    queue = []
    visited[start] = True
    queue.append(start)
    res = []
    while queue:
        ind_v = queue.pop(0)
        res.append(ind_v)
        for i,el in enumerate(graph[ind_v]):
            if not visited[i] and el:
                visited[i] = True
                queue.append(i)
    return res

def adjacency_matrix_radius(graph: list[list]) -> int:
    """
    :param list[list] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    """

    def bfs_distance(start: int) -> list[int]:
        """
        BFS to calculate distances from the start vertex
        :param int start: index of edge, from which we move
        :return list[int]: list of the distance from the starting vertex to all adjacent vertices
        """
        visited = [False] * len(graph)
        distance = [float('inf')] * len(graph)
        queue = []

        queue.append(start)
        visited[start] = True
        distance[start] = 0

        while queue:
            ind_v = queue.pop(0)
            for i, el in enumerate(graph[ind_v]):
                if el and not visited[i]:
                    visited[i] = True
                    distance[i] = distance[ind_v] + 1
                    queue.append(i)
        return distance

    eccentricities = [max(bfs_distance(i)) for i in range(len(graph))]

    return min(eccentricities)

def adjacency_dict_radius(graph: dict[int: list[int]]) -> int:
    """
    :param dict graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [1]})
    2
    """
    def bfs_distance(start: int) -> list[int]:
        """
        BFS to calculate distances from the start vertex
        :param int start: index of edge, from which we move
        :return list[int]: list of the distance from the starting vertex to all adjacent vertices
        """
        visited = [False] * len(graph)
        distance = [float('inf')] * len(graph)
        queue = []

        queue.append(start)
        visited[start] = True
        distance[start] = 0

        while queue:
            ind_v = queue.pop(0)
            for ind in graph[ind_v]:
                if not visited[ind]:
                    visited[ind] = True
                    distance[ind] = distance[ind_v] + 1
                    queue.append(ind)
        return distance

    eccentricities = [max(bfs_distance(key)) for key in graph]

    return min(eccentricities)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
