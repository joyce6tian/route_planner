import math, numpy as np
from queue import PriorityQueue

def heuristic_distance(start, goal):
    """start and goal are intersection of map"""
    d = math.sqrt((start[0] - goal[0])**2+ (start[1] - goal[1])**2)
    return d

def generate_path(previous,start, goal):
    current  = goal
    path = [current]
    while current!=start:
        current = previous[current]
        path.append(current)

    path.reverse()
    return path


def path_length_calculation(mapp, lst):    
    dist = 0
    for i in range(len(lst)-1):
        dist += heuristic_distance(mapp.intersections[lst[i]], mapp.intersections[lst[i]+1])
    return dist


def shortest_path(mapp, start, goal):
    queue = PriorityQueue()
    queue.put((0, start))

    score = {start: 0}
    previous = {start: None}
    closed = []
    h = [heuristic_distance(mapp.intersections[node], mapp.intersections[goal]) for node in range(len(mapp.roads))]

    while not queue.empty():
        _, current = queue.get()
        if current == goal:
             return generate_path(previous, start, goal)
        for node in mapp.roads[current]:
             if node not in closed:
                g = score[current] + heuristic_distance(mapp.intersections[current], mapp.intersections[node])
                f = g+h[node]
                if (node not in score) or (g < score[node]):
                    score[node] = g
                    queue.put((f, node))
                    previous[node] = current
        closed.append(current)

    return generate_path(previous, start, goal)