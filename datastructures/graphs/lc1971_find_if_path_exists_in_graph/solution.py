"""
1971. Find if Path Exists in Graph
Understand the Question:  Given a bidirectional graph (represented by a list of edges, 
where each edge-list contains a origin and destination vertex), a source vertex,
and destination vertex.  Return a True if there is a path from the source to the
destination vertex, otherwise return False.

Clarifying questions:
1. Could I have an empty graph?
2. Will the graph fit in memory?
3. Could the source == destination? There are no self edges
4. are all edges guaranteed to be bidirectional? yes

Examples
https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

Brainstorm ideas:
1. BFS approach: start from the source node see if there is a path to destination.
    Have a queue and set to keep track of each vertex of its immediate neighbors
    and a visited set to ensure I'm only checking neighbors once.
    traverse the graph checking if the current node I'm on is the destination 
    node, return True if yes, False if I've traversed the whole graph without
    finding it.
2. Could do a DFS search here but could find a shorter path with BFS

"""

from collections import deque, defaultdict

def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if n == 0 or (len(edges) == 1 and edges[0][0] == edges[0][1]):
            return False
        
        graph = defaultdict(set)
        # creating a dict representation of graph, easier for me to read and search/access later.
        for i in range(len(edges)):
            graph[edges[i][0]].add(edges[i][1])
            graph[edges[i][1]].add(edges[i][0])
        # print(graph)

        search_queue  = deque()
        visited = set()
        search_queue.append(source)
        visited.add(source)

        while search_queue:
            source_destination = search_queue.popleft()
            # print(f'source_destination: {source_destination}')
            if destination == source_destination:
                return True #there is a path!
            for elem in graph[source_destination]:
                if elem not in visited:
                    search_queue.append(elem)   
                    visited.add(elem)

        return False # did not find destination vertex

def main():
    assert valid_path(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2) == True
    assert valid_path(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5) == False
    assert valid_path(n = 1, edges = [], source = 0, destination = 0) == True
    assert valid_path(n = 1, edges = [[0,0]], source = 0, destination = 0) == False
    assert valid_path(n = 0, edges = [], source = None, destination = None) == False
    print("assertion tests passed!")


if __name__ == "__main__":
    main()