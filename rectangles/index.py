'''
https://www.interviewcake.com/question/rectangular-love
'''
from random import shuffle

class Rectangle(object):
    def __init__(self, hash):
        self.hash = hash
        self.bottom_left = (self.hash["x"], self.hash["y"])
        self.bottom_right = (self.hash["x"] + self.hash["width"], self.hash["y"])
        self.top_left = (self.hash["x"], self.hash["y"] + self.hash["height"])
        self.top_right = (self.hash["x"] + self.hash["width"], self.hash["y"] + self.hash["height"])

def find_intersection(rectangles):
    rectangles = map(lambda rectangle: Rectangle(rectangle), rectangles)

    if rectangles[0].bottom_left[0] <= rectangles[1].bottom_left[0]:
        left_edge = rectangles[1].bottom_left[0]
        right_edge = rectangles[0].bottom_right[0]
    else:
        left_edge = rectangles[0].bottom_left[0]
        right_edge = rectangles[1].bottom_right[0]

    print left_edge, right_edge

rectangles = [
    {'x': 0, 'y': 0, 'width': 100, 'height': 40},
    {'x': 80, 'y': 30, 'width': 30, 'height': 50}
]

shuffle(rectangles)

print find_intersection(rectangles)
