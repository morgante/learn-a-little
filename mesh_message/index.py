'''
https://www.interviewcake.com/question/python/mesh-message
'''
from queue import Queue

def find_shortest_path_recursive(network, origin, destination, visited=None):
    if origin is destination:
        return [origin, ]

    if visited is None:
        visited = [origin]
    else:
        visited = visited + [origin, ]

    try:
        neighbors = network[origin]
    except KeyError:
        return None

    if destination in neighbors:
        return visited + [destination, ]

    shortest_path = None
    for neighbor in neighbors:
        if neighbor not in visited:
            new_path = find_shortest_path_recursive(network, neighbor, destination, visited)
            if new_path:
                if not shortest_path:
                    shortest_path = new_path
                else:
                    if len(new_path) < len(shortest_path):
                        shortest_path = new_path

    return shortest_path

def find_shortest_path_unrecursive(network, origin, destination):
    remaining_nodes = Queue()
    remaining_nodes.put(origin)

    if origin is destination:
        return [origin, ]

    visited = {
        origin: None
    }

    while not remaining_nodes.empty():
        node = remaining_nodes.get()

        if node is destination:
            my_path = []
            path_node = node

            while path_node:
                my_path.append(path_node)
                path_node = visited[path_node]

            return list(reversed(my_path))

        try:
            for neighbor in network[node]:
                if neighbor not in visited:
                    remaining_nodes.put(neighbor)
                    visited[neighbor] = node
        except KeyError:
            pass

def find_shortest_path(network, origin, destination, recursive=False):
    if recursive:
        return find_shortest_path_recursive(network, origin, destination)
    else:
        return find_shortest_path_unrecursive(network, origin, destination)

network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min'],
    'Jayden'  : ['Min', 'Amelia', 'Ren'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
}

# print(find_shortest_path(network, 'Jayden', 'Adam'))
print(find_shortest_path(network, 'Miguel', 'Ren', True),
    find_shortest_path(network, 'Miguel', 'Ren', False))
print(find_shortest_path(network, 'Miguel', 'Noam', False))
print(find_shortest_path(network, 'Miguel', 'Miguel', False))
