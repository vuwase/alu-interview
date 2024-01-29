def rain(walls):
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(n):
        water_at_wall = min(left_max[i], right_max[i]) - walls[i]
        total_water += max(0, water_at_wall)

    return total_water

# Example usage
walls1 = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls1))  # Output: 6

walls2 = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls2))  # Output: 6

