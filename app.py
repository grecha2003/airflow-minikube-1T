def generate_pascals_triangle(levels):
    triangle = [[1]]
    for i in range(1, levels):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

pascals_triangle = generate_pascals_triangle(10)
for row in pascals_triangle:
    print(' '.join(map(str, row)))
