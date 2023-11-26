
#!/usr/bin/python3
"""
12. Pascal Triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascals triangle of n:
    """
    if n <= 0:
        return []

    triangles = [[1]]

    if n == 1:
        return triangles
    
    while len(triangles) < n:
            last_row = triangles[-1]
            new_row = [1]
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])
            new_row.append(1)
            triangles.append(new_row)

    return triangles
