'''
https://www.interviewcake.com/question/cake-thief
'''

class Bag:
    def __init__(self):
        self.cakes = []
    def add_cake(self, cake):
        self.cakes.append(cake)
    def get_weight(self):
        return reduce(lambda memo, cake: memo + cake[0], self.cakes, 0)

def max_duffel_bag_value(cakes, capacity):
    options = []

    for cake in cakes:
        added = 0
        while added * cake[0] <= capacity:
            bag = Bag()
            for x in range(0, added):
                bag.add_cake(cake)
            options.append(bag)
            added += 1

    for bag in options:
        print bag.cakes



cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

max_duffel_bag_value(cake_tuples, capacity)
