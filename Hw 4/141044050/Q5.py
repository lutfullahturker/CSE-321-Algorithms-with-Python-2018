from collections import defaultdict


def dfs(graph, root, find, visited = None):
    if visited is None:
        visited = set()
    if root == find:
        return True
    visited.add(root)
    for next in graph[root] - visited:
        if dfs(graph, next, find, visited):
            return True
    return False


def constraintsControl(graph,vertexes,consts):
    for i in range(len(consts)):
        tmp = consts[i]
        if tmp[1] == '=':
            if tmp[0] not in vertexes:
                vertexes.add(tmp[0])
            if tmp[2] not in vertexes:
                vertexes.add(tmp[2])
            graph[tmp[0]].add(tmp[2])
            graph[tmp[2]].add(tmp[0])

        elif tmp[1] == '!':
            if (tmp[0] not in vertexes) or (tmp[2] not in vertexes):
                continue
            if dfs(graph, tmp[0], tmp[2]):
                return False
        else:
            print('Constraints String Array is Wrong !')
    return True


def main():
    graph = defaultdict(set)
    vertexes = set()
    constraints = ['x=y', 'y=z', 'z=t', 't!x']
    if constraintsControl(graph,vertexes,constraints):
        print(constraints)
        print('The constraints can be satisfied')
    else:
        print(constraints)
        print('The constraints cannot be satisfied')


if __name__ == '__main__':
    main()
