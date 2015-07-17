'''
https://www.interviewcake.com/question/cake-thief
'''

class Bag:
    def __init__(self):
        self.cakes = []
    def add(self, cake):
        self.cakes.append(cake)
    def get_weight(self):
        return reduce(lambda memo, cake: memo + cake[0], self.cakes, 0)
    def get_value(self):
        return reduce(lambda memo, cake: memo + cake[1], self.cakes, 0)

def max_duffel_bag_value(cakes, capacity):
    if len(cakes) < 1:
        return 0

    options = []

    cakes.sort(key=lambda cake: cake[1] / cake[0], reverse=True)

    bag = Bag()

    while bag.get_weight() <= capacity - cakes[0][0]:
        bag.add(cakes[0])

    another_bag = max_duffel_bag_value(cakes[1:], capacity - bag.get_weight())

    return another_bag + bag.get_value()

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20

print max_duffel_bag_value(cake_tuples, capacity)
