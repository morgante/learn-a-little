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
    max_values = [0] * (capacity + 1)
    max_value = 0

    for analyze_capacity in xrange(capacity + 1):
        current_max = 0
        for weight, value in cakes:
            if weight < 1 and value > 0:
                return "infinity"
            elif weight < 1 and value == 1:
                pass
            elif weight <= analyze_capacity:
                additional_capacity = analyze_capacity - weight
                potential_max = max_values[additional_capacity] + value
                current_max = max(potential_max, current_max)

        max_values[analyze_capacity] = current_max

    return max_values[capacity]



print max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 20)
print max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 0)
print max_duffel_bag_value([(7, 160), (3, 90), (0, 15)], 0)
print max_duffel_bag_value([(7, 160), (3, 90), (0, 15)], 50)
print max_duffel_bag_value([(7, 160), (3, 90), (0, 0)], 50)
