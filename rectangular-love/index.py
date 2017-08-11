'''
https://www.interviewcake.com/question/rectangular-love
'''
from random import shuffle, sample

class Rectangle(object):
    def __init__(self, dictionary=None, left=None, right=None, top=None, bottom=None):
        if (dictionary is not None):
            self.dictionary = dictionary
        else:
            self.dictionary = {
                "x": left,
                "y": bottom,
                "height": top - bottom,
                "width": right - left
            }
        self.bottom_left = (self.dictionary["x"], self.dictionary["y"])
        self.bottom_right = (self.dictionary["x"] + self.dictionary["width"], self.dictionary["y"])
        self.top_left = (self.dictionary["x"], self.dictionary["y"] + self.dictionary["height"])
        self.top_right = (self.dictionary["x"] + self.dictionary["width"], self.dictionary["y"] + self.dictionary["height"])

def find_intersection(rectangles):
    rectangles = map(lambda rectangle: Rectangle(dictionary=rectangle), rectangles)

    left_edge = max(rectangles[0].bottom_left[0], rectangles[1].bottom_left[0])
    right_edge = min(rectangles[0].bottom_right[0], rectangles[1].bottom_right[0])
    bottom_edge = max(rectangles[0].bottom_left[1], rectangles[1].bottom_left[1])
    top_edge = min(rectangles[0].top_left[1], rectangles[1].top_left[1])

    if left_edge > right_edge or bottom_edge > top_edge:
        return None
    else:
        overlap = Rectangle(left=left_edge, bottom=bottom_edge, top=top_edge, right=right_edge)
        return overlap.dictionary


print find_intersection(({'x': 0, 'y': 0, 'width': 100, 'height': 40},{'x': 80, 'y': 30, 'width': 30, 'height': 50}))
print find_intersection(({'x': 0, 'y': 5, 'width': 10, 'height': 10},{'x': 80, 'y': 30, 'width': 30, 'height': 50}))
print find_intersection(({'x': 0, 'y': 0, 'width': 100, 'height': 100},{'x': 10, 'y': 10, 'width': 10, 'height': 10}))
print find_intersection(({'x': 0, 'y': 0, 'width': 100, 'height': 100},{'x': 10, 'y': 10, 'width': 10, 'height': 200}))
print find_intersection(({'x': 0, 'y': 0, 'width': 100, 'height': 100},{'x': 10, 'y': 10, 'width': 200, 'height': 10}))
