import math

import pygame as pygame

from Space import *
from Constants import *

TIME_WAITING = 80

def DFS(g: Graph, sc: pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1] * g.get_len()

    # TODO: Implement DFS algorithm using open_set, closed_set, and father
    while open_set:
        current = g.grid_cells[open_set.pop()]
        closed_set.append(current.value)
        current.set_color(yellow)
        current.draw(sc)
        pygame.display.update()
        pygame.time.wait(TIME_WAITING)
        if g.is_goal(current):
            print("Found")
            current.set_color(purple)
            g.start.set_color(orange)
            current.draw(sc)
            g.start.draw(sc)
            pygame.display.update()
            pygame.time.wait(TIME_WAITING)
            # Color path
            while father[current.value] != -1:
                x1, y1 = current.x, current.y
                temp=current
                current = g.grid_cells[father[current.value]]
                x2, y2 = current.x, current.y
                pygame.draw.line(sc, green, (x1, y1), (x2, y2))
                temp.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
                if father[current.value] == -1:
                    break
                current.set_color(grey)
                current.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
            g.start.draw(sc)
            pygame.display.update()
            pygame.time.wait(TIME_WAITING)
            return
        for neighbor in g.get_neighbors(current):
            if neighbor.value not in open_set and neighbor.value not in closed_set:
                father[neighbor.value] = current.value
                open_set.append(neighbor.value)
                neighbor.set_color(red)
                neighbor.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
        current.set_color(blue)
        current.draw(sc)
        pygame.display.update()
        pygame.time.wait(TIME_WAITING)
    print("Not found")
    raise NotImplementedError('Not implemented')


def BFS(g: Graph, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1] * g.get_len()

    # TODO: Implement BFS algorithm using open_set, closed_set, and father
    while open_set:
        current = g.grid_cells[open_set.pop(0)]
        closed_set.append(current.value)
        current.set_color(yellow)
        current.draw(sc)
        pygame.display.update()
        pygame.time.wait(TIME_WAITING)
        if g.is_goal(current):
            print("Found")
            current.set_color(purple)
            g.start.set_color(orange)
            current.draw(sc)
            g.start.draw(sc)
            pygame.display.update()
            pygame.time.wait(TIME_WAITING)
            # Color path
            while father[current.value] != -1:
                x1, y1 = current.x, current.y
                temp=current
                current = g.grid_cells[father[current.value]]
                x2, y2 = current.x, current.y
                pygame.draw.line(sc, green, (x1, y1), (x2, y2))
                temp.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
                if father[current.value] == -1:
                    break
                current.set_color(grey)
                current.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
            g.start.draw(sc)
            pygame.display.update()
            pygame.time.wait(TIME_WAITING)
            return
        for neighbor in g.get_neighbors(current):
            if neighbor.value not in open_set and neighbor.value not in closed_set:
                father[neighbor.value] = current.value
                open_set.append(neighbor.value)
                neighbor.set_color(red)
                neighbor.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
        current.set_color(blue)
        current.draw(sc)
        pygame.display.update()
        pygame.time.wait(TIME_WAITING)
    print("Not found")
    raise NotImplementedError('Not implemented')


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1] * g.get_len()
    cost = [100_000] * g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    while open_set:
        current=g.grid_cells[min(open_set, key=open_set.get)]
        del open_set[current.value]
        closed_set.append(current.value)
        current.set_color(yellow)
        current.draw(sc)
        pygame.display.update()
        pygame.time.wait(TIME_WAITING)
        if g.is_goal(current):
            print("Found")
            current.set_color(purple)
            g.start.set_color(orange)
            current.draw(sc)
            g.start.draw(sc)
            pygame.display.update()
            pygame.time.wait(TIME_WAITING)
            # Color path
            while father[current.value] != -1:
                x1, y1 = current.x, current.y
                temp = current
                current = g.grid_cells[father[current.value]]
                x2, y2 = current.x, current.y
                pygame.draw.line(sc, green, (x1, y1), (x2, y2))
                temp.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
                if father[current.value] == -1:
                    break
                current.set_color(grey)
                current.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
            g.start.draw(sc)
            pygame.display.update()
            pygame.time.wait(TIME_WAITING)
            return
        for neighbor in g.get_neighbors(current):
            step_cost = math.sqrt((current.x-neighbor.x)*(current.x-neighbor.x)+(current.y-neighbor.y)*(current.y-neighbor.y))
            if neighbor.value not in closed_set:
                tentative_cost = cost[current.value] + step_cost
                if tentative_cost < cost[neighbor.value]:
                    cost[neighbor.value] = tentative_cost
                    father[neighbor.value] = current.value
                    open_set[neighbor.value] = tentative_cost
                    neighbor.set_color(red)
                    neighbor.draw(sc)
                    pygame.display.update()
                    pygame.time.wait(TIME_WAITING)
        current.set_color(blue)
        current.draw(sc)
        pygame.display.update()
        pygame.time.wait(TIME_WAITING)
    print("Not found")
    raise NotImplementedError('Not implemented')


def manhattan_distance(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1] * g.get_len()
    cost = [100_000] * g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement A* algorithm using open_set, closed_set, and father
    while open_set:
        current=g.grid_cells[min(open_set, key=open_set.get)]
        del open_set[current.value]
        closed_set.append(current.value)
        current.set_color(yellow)
        current.draw(sc)
        pygame.display.update()
        pygame.time.wait(TIME_WAITING)
        if g.is_goal(current):
            print("Found")
            current.set_color(purple)
            g.start.set_color(orange)
            current.draw(sc)
            g.start.draw(sc)
            pygame.display.update()
            pygame.time.wait(TIME_WAITING)
            # Color path
            while father[current.value] != -1:
                x1, y1 = current.x, current.y
                temp = current
                current = g.grid_cells[father[current.value]]
                x2, y2 = current.x, current.y
                pygame.draw.line(sc, green, (x1, y1), (x2, y2))
                temp.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
                if father[current.value] == -1:
                    break
                current.set_color(grey)
                current.draw(sc)
                pygame.display.update()
                pygame.time.wait(TIME_WAITING)
            g.start.draw(sc)
            pygame.display.update()
            pygame.time.wait(TIME_WAITING)
            return
        for neighbor in g.get_neighbors(current):
            if neighbor.value not in closed_set:
                tentative_cost = cost[current.value] + 1
                if tentative_cost < cost[neighbor.value]:
                    cost[neighbor.value] = tentative_cost
                    father[neighbor.value] = current.value
                    f_cost=tentative_cost+manhattan_distance(neighbor, g.goal)
                    open_set[neighbor.value] = f_cost
                    neighbor.set_color(red)
                    neighbor.draw(sc)
                    pygame.display.update()
                    pygame.time.wait(TIME_WAITING)
        current.set_color(blue)
        current.draw(sc)
        pygame.display.update()
        pygame.time.wait(TIME_WAITING)
    print("Not found")

    raise NotImplementedError('Not implemented')
