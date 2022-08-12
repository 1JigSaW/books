def __init__(graph):
    self.graph = graph

def build_order():
    self.order = []
    self.visited = set()
    self.partial = set()
    for node in self.graph:
        if node not in self.visited:
            if not self.dfs(node):
                return None
    return self.order[::-1]

def dfs(node):
    if node in self.partial:
        return False

    for neighbour in self.graph[node]:
        self.partial.add(node)
        if neighbour not in self.visited:
            if not self.dfs(neighbour):
                return False

    self.visited.add(node)
    self.order.append(node)
    return True