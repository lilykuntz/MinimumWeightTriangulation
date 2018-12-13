
# Lillian Kuntz
# CS 302 Implementation Project2
# Minimum Weight Triangulation

import random
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


#to find minimum of two double values
def min(x, y):
    if x<= y:
        return x
    else:
        return y

#to find distance between two points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) +(p1[1] - p2[1])*(p1[1] - p2[1]))

#to find cost of a triangle (perimeter)
def cost(points, i, j, k):
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1)

def generate_points(center_x, center_y, mean_radius, sigma_radius, num_points):

    points = []
    for theta in np.linspace(2*math.pi - (2*math.pi/num_points), 0, num_points):
        radius = random.gauss(mean_radius, sigma_radius)
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        points.append([x,y])
    return points

#to find min cost of polygon triangulation
def MWT(points, n):

    for m in range(n):
        x = points[m][0]
        y = points[m][1]
        plt.plot(x, y, 'bo')
        plt.text(x * (1 + 0.01), y * (1 + 0.01) , m, fontsize=10)
        if m == n - 1:
            m = -1
        x, y = [points[m][0], points[m+1][0]], [points[m][1], points[m+1][1]]
        plt.plot(x, y, marker = 'o')
        plt.draw()

    if n < 3:
        return 0
    columns = [x for x in range(len(points))]
    rows = [x for x in range(len(points))]
    n_rows = len(points)
    table = []
    ktable = []
    for row in range(n_rows):
        table.append([math.inf] * len(points))
        ktable.append([-1] * len(points))

    gap = 0
    while gap < n:
        i = 0
        j = gap
        while j < n:
            if j < (i + 2):
                table[i][j] = 0
                the_table = plt.table(cellText=table,rowLabels=rows,colLabels=columns,loc='bottom')
                the_table._cells[(i + 1,j)].set_facecolor("#56b5fd")

            else:
                table[i][j] = math.inf
                k = i + 1
                while k < j:
                    val = int(round(table[i][k] + table[k][j] + cost(points,i,j,k)))
                    if table[i][j] > val:
                        table[i][j] = val
                        ktable[i][j] = k
                        the_table = plt.table(cellText=table,rowLabels=rows,colLabels=columns, loc='bottom')
                        the_table._cells[(i + 1, j)].set_facecolor("#56b5fd")
                        the_table._cells[(i + 1, k)].set_facecolor("red")
                        the_table._cells[(k + 1, j)].set_facecolor("red")
                        the_ktable = plt.table(cellText=ktable,rowLabels=rows,colLabels=columns, loc='top')
                        the_ktable._cells[(i + 1, j)].set_facecolor("#56b5fd")
                        plt.draw()
                        plt.pause(0.01)
                    k = k + 1
            i = i + 1
            j = j + 1
        gap = gap + 1



    for a in range (0,n):
        for b in range (0,n):
            if table[a][b] == math.inf:
                table[a][b] = None

    p = []
    for x in range(n):
        p.append(x)

    j = n-1

    the_table = plt.table(cellText=table,rowLabels=rows,colLabels=columns, loc='bottom')
    the_ktable = plt.table(cellText=ktable,rowLabels=rows,colLabels=columns, loc='top')


    # Adjust layout to make room for the table:

    draw(0, j, int(round(ktable[0][n-1])), table, the_table, ktable, the_ktable, points)

#draw the triangulation
def draw(i, j, k, table, the_table, ktable, the_ktable, points):

    the_ktable._cells[(i + 1, j)].set_facecolor("yellow")
    plt.draw()
    plt.pause(0.01)

    n = len(points) -1

    i = int(round(i))
    j = int(round(j))
    k = int(round(k))

    x, y = [points[i][0], points[j][0]], [points[i][1], points[j][1]]
    x1, y1 = [points[i][0], points[k][0]], [points[i][1], points[k][1]]
    plt.plot(x, y, x1, y1, marker = 'o')
    plt.draw()
    plt.pause(0.01)

    if j >= 0:
        if ktable[k][j] >= 0:
            draw(k, j, ktable[k][j], table, the_table, ktable,the_ktable, points)
        if ktable[i][k] >= 0:
            draw(i, k, ktable[i][k], table, the_table, ktable, the_ktable, points)


n = input("Enter number of points: ")
n = int(n)
type(n)
points = generate_points(5.0, 7.0, 1.0, 0.1, n)
plt.subplots_adjust(left=0.2, bottom=0.3, top = 0.7)
plt.yticks([])
plt.xticks([])

MWT(points, n)

x, y = [points[0][0], points[1][0]], [points[0][1], points[1][1]]
plt.plot(x, y, marker = 'o')
plt.show()
