"""Traveling Salesman Problem

"""
import os
import random
import numpy as np
# set the seed
np.random.seed(42)


city_dict = {}
with open('Term 1/Metaheuristics/01-Lab1/TSP dataset/dummy_data.tsp', 'r') as f:
    next(f)
    for line in f:
        
        values = line.split()
        city_dict[int(values[0])] = [float(i) for i in values[1:]]


def euc_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

visited = [np.random.choice(list(city_dict.keys()))] # selecting a random city id
not_visited = [c_id for c_id in city_dict.keys() if c_id not in visited]
total_distance = []
print(f'initial visited list: {visited}')
print(f'initial not visited list {not_visited}')
for _ in range(len(city_dict)-1):
    distances = {}
    for city in not_visited:
        x1, y1 = city_dict[visited[-1]]
        x2, y2 = city_dict[city]
        dist = euc_distance(x1, y1, x2, y2)
        distances[city] = dist

    min_dist_id = min(distances, key=distances.get)
    min_dist = min(distances.values())
    total_distance.append(min_dist)
    visited.append(min_dist_id)
    
    if min_dist_id in not_visited:
        not_visited.remove(min_dist_id)
    print(f"Visited: {visited}")
    print(f'not_visited {not_visited}')
    print('\n')

print(f"Final Visited: {visited}")
print(f"Final Not Visited: {not_visited}")
print(f"Total Distance: {sum(total_distance)}")



