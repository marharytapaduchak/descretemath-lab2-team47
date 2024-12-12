"""
Lab 2
"""

def read_incidence_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the incidence matrix of a given graph
    """
    pass


def read_adjacency_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the adjacency matrix of a given graph
    """
    pass


def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict: the adjacency dict of a given graph
    """
    pass


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
    pass


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
    pass


def recursive_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    pass


def recursive_adjacency_matrix_dfs(graph: list[list[int]], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass


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
