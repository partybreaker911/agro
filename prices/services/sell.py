from dataclasses import dataclass
from typing import List
from itertools import product
import numpy as np
import pandas as pd

"""
    Formula 1+(1/A-1)*(1+B)*C
    where A is product quantity,
    B is an margin,
    C is cost
"""


@dataclass
class Sell:
    margin: List[float]
    quantity: List[float]
    cost: List[float]
    # matrix: List[]

    def get_matrix(self):
        """
        [[0, 0, 0, 0, 0], [-2, -2, -2, -2, -2], [-4, -4, -4, -4, -4], [-6, -6, -6, -6, -6]]
        """
        matrix = []
        for i in range(len(self.margin)):
            row = []
            for j in range(len(self.quantity)):
                row.append(self.margin[i])
            matrix.append(row)
        return matrix

    def get_percentage(self):
        result = []
        matrix = self.get_matrix()
        first = [(1 + (1 / x - 1)) for x in self.quantity]
        second = [(x * y) for x, y in zip(first, self.cost)]
        # for i
        return second

    # def second_step(self):
    #     return [(1 + x) for x in self.margin]

    # def get_matrix(self):
    # return [(x * y) for x, y in product(self.second_step(), self.first_step())]


margin = [0, -2, -4, -6]
quantity = [100, 97, 94, 91, 88]
cost = [100, 99, 97, 96, 100]

# # print(cost)
# result = []
# for i, j in zip(quantity, cost):
#     r = 1 + (1 / i - 1) * j
#     result.append(r)
# print(result)
# result2 = []
# for i, j in product(margin, result):
#     r = (1 + i) * j
#     result2.append(r)
data = Sell(margin, quantity, cost).get_matrix()
values = Sell(margin, quantity, cost).get_percentage()
result_matrix = []
for i in range(len(data)):
    row = []
    for j in range(len(data[i])):
        row.append((1 + data[i][j]) * values[j])
    result_matrix.append(row)
print(result_matrix)
# print(result2)
# df = pd.DataFrame(data, columns=quantity)
# print(df.to_string(index=False))
