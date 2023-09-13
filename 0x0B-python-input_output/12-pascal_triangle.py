#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """returns a list of a list of integer"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trig = triangles[-1]
        m = [1]
        for i in range(len(trig) - 1):
            m.append(trig[i] + trig[i + 1])
        m.append(1)
        triangles.append(m)
    return triangles
