'''
https://www.interviewcake.com/question/python/rectangular-love
'''

def find_range_intersect(rects, start_var, length_var):
    if rects[0].get(start_var) <= rects[1].get(start_var):
        left_rec = rects[0]
        right_rec = rects[1]
    else:
        left_rec = rects[1]
        right_rec = rects[0]

    right_edge = min(
        left_rec.get(start_var) + left_rec.get(length_var),
        right_rec.get(start_var) + right_rec.get(length_var))
    left_edge = right_rec.get(start_var)

    if right_edge < left_edge:
        return None

    return (left_edge, right_edge)

def find_intersection(rects):
    try:
        (left_edge, right_edge) = find_range_intersect(rects, 'x', 'width')
        (top_edge, bottom_edge) = find_range_intersect(rects, 'y', 'height')
    except TypeError:
        return None

    return {
        'x': left_edge,
        'height': bottom_edge - top_edge,
        'width': right_edge - left_edge,
        'y': top_edge,
    }

print(find_intersection(({'x': 0, 'y': 0, 'width': 100, 'height': 40},{'x': 80, 'y': 30, 'width': 30, 'height': 50})))
print(find_intersection(({'x': 0, 'y': 5, 'width': 10, 'height': 10},{'x': 80, 'y': 30, 'width': 30, 'height': 50})))
print(find_intersection(({'x': 0, 'y': 0, 'width': 100, 'height': 100},{'x': 10, 'y': 10, 'width': 10, 'height': 10})))
print(find_intersection(({'x': 0, 'y': 0, 'width': 100, 'height': 100},{'x': 10, 'y': 10, 'width': 10, 'height': 200})))
print(find_intersection(({'x': 0, 'y': 0, 'width': 100, 'height': 100},{'x': 10, 'y': 10, 'width': 200, 'height': 10})))
