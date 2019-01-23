import collections
import os.path
import xlrd
from pip._vendor.distlib.compat import raw_input


def readAndFill(graph, vertexes, path):
    if not os.path.isfile(path):
        print("File doesn't exist. Please  enter Full Path from root")
        return False
    book = xlrd.open_workbook(path)
    excelFile = book.sheet_by_index(0)
    numOfCols = excelFile.ncols
    numOfRows = excelFile.nrows


    for row_idx in range(3, numOfRows):
        for col_idx in range(0, numOfCols):
            if excelFile.cell(row_idx, col_idx).value not in vertexes :
                vertexes.add(excelFile.cell(row_idx, col_idx).value)
                graph[excelFile.cell(row_idx, col_idx).value] = set()
            if col_idx == 0:
                graph[excelFile.cell(row_idx, col_idx).value].add(excelFile.cell(row_idx, 1).value)
    return excelFile.cell(0, 1).value


def dfs(graph, root, visited = None):
    if visited is None:
        visited = set()
    if root not in visited:
        print("%s -> " % root,end='')
    visited.add(root)
    for next in graph[root] - visited:
        dfs(graph, next, visited)
    return visited


def bfs(graph, root):
    visited, queue = {root}, collections.deque([root])
    while queue:
        vertex = queue.popleft()
        print("%s -> " % vertex, end='')
        for node in graph[vertex]:
            if node not in visited:
                visited.add(node)
                queue.append(node)


def main():
    filePath = raw_input("Enter the full path of the Excel File\n")
    graph = {}
    vertexes = set()
    root = readAndFill(graph, vertexes, filePath)
    if root == False:
        return
    print("DFS")
    print("-" * 40)
    dfs(graph, root)
    print()
    print("-" * 40)
    print("BFS")
    print("-" * 40)
    bfs(graph, root)
    print()
    print("-" * 40)


if __name__ == '__main__':
    main()
