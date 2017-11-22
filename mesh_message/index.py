'''
https://www.interviewcake.com/question/python/mesh-message
'''

def find_shortest_path(network, origin, destination, visited=None):
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
            new_path = find_shortest_path(network, neighbor, destination, visited)
            if new_path:
                if not shortest_path:
                    shortest_path = new_path
                else:
                    if len(new_path) < len(shortest_path):
                        shortest_path = new_path

    return shortest_path

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
print(find_shortest_path(network, 'Miguel', 'Ren'))
print(find_shortest_path(network, 'Miguel', 'Noam'))
