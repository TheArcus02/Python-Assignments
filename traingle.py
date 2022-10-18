"""
You are given  points on a plane. You have to find two triangles:
- one with the smallest area
- one with the biggest area
- The triangles cannot be degenerated (a degenerated triangle is formed by 3
  colinear points, or when its area is equal to zero).

Input Format
The first line of input contains integer N.
Each of the N following lines contains two space-separated
integers xi, yi - the coordinates of i-th point.

Constraints
 3 <= N <= 20
-100 <= xi, yi <= 100

Output Format
Two space separated numbers:
- the area of the triangle with the smallest area
- the area of the triangle with the biggest area

Do not round the results.
"""

def get_points():
    points_count = int(input(''))

    points = []
    for i in range(points_count):
        point = str(input(''))
        coordinates = point.split(' ')
        x = int(coordinates[0])
        y = int(coordinates[1])
        points.append([x, y])
    return points


def get_triangles(points: list):
    possible_triangles = []

    for i in range(len(points)):
        cords1 = points[i]
        sliced_points = points[i+1:]

        for j in range(len(sliced_points)):
            cords2 = sliced_points[j]
            sliced_points_twice = sliced_points[j + 1:]

            for k in range(len(sliced_points_twice)):
                cords3 = sliced_points_twice[k]
                possible_triangles.append([cords1, cords2, cords3])

    return possible_triangles


def get_areas(triangles: list):

    areas = []

    for triangle in triangles:
        x1 = triangle[1][0] - triangle[0][0]
        y1 = triangle[1][1] - triangle[0][1]

        x2 = triangle[2][0] - triangle[0][0]
        y2 = triangle[2][1] - triangle[0][1]

        area = abs(x1*y2 - y1*x2)/2
        areas.append(area)

    min_area = min(areas)
    max_area = max(areas)

    return min_area, max_area


def main():

    points = get_points()
    triangles = get_triangles(points)
    print(triangles)
    min_area, max_area = get_areas(triangles)
    print(min_area, max_area)

main()
