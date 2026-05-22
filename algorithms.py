import networkx as nx

# =========================================================
# BFS
# =========================================================
def bfs(graph, start, goal):

    try:

        return nx.shortest_path(
            graph,
            source=start,
            target=goal
        )

    except Exception:

        return None

# =========================================================
# DFS
# =========================================================
def dfs(graph, start, goal):

    try:


        stack = [(start, [start])]

        LIMIT = 3000

        while stack:

            node, path = stack.pop()

            if len(path) > LIMIT:
                continue

            if node == goal:
                return path

            if node not in visited:

                visited.add(node)

                for neighbor in graph.neighbors(node):

                    if neighbor not in visited:

                        stack.append(
                            (
                                neighbor,
                                path + [neighbor]
                            )
                        )

        return None

    except Exception:

        return None

# =========================================================
# A*
# =========================================================
def astar(graph, start, goal):

    try:

        return nx.astar_path(
            graph,
            start,
            goal,
            weight="length"
        )

    except Exception:

        return None