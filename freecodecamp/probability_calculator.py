# Freecodecamp - Scientific Calc. Python - Project No. 5

import copy
import random

class Hat:
    def __init__(self, **kwargs): #kwargs work better than args
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
            
    def __str__(self):
        return f"{self.contents}"
    
    def draw(self, drawn):
        if drawn >= len(self.contents):
            all_balls = self.contents.copy()
            self.contents.clear()
            return all_balls
        else:
            new_list = []
            for _ in range(drawn):
                index = random.randint(0, len(self.contents) - 1)
                new_list.append(self.contents.pop(index))
            return new_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if isinstance(hat,Hat):
        succes = 0
        for i in range(num_experiments):
            hat_copy = copy.deepcopy(hat)
            actual_draw = hat_copy.draw(num_balls_drawn)
            drawn_dict = {}
            for color in actual_draw:
                if color not in drawn_dict:
                    drawn_dict[color] = 1
                else:
                    drawn_dict[color] += 1
            for key, value in expected_balls.items():
                if drawn_dict.get(key, 0) < value:
                    break
            else:
                succes += 1
        probability = succes / num_experiments
        return probability
            
