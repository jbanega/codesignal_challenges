def solution(numbers):
    """This function checks if each 3x3 submatrix from a 3xN matrix
    contains all digits from 1 to 9"""

    solution = []
    row_lenght = len(numbers[0])
    
    i = 0
    while i < (row_lenght - 2):
        window_numbers = []
        for row in numbers:
            digits = row[i: i+3]
            for d in digits:
                window_numbers.append(d)

        flag = True
        for n in range(1, 10):
            if n not in window_numbers:
                flag = False
                break
        solution.append(flag)
        print(f"Numbers of submatrix {i + 1}: {sorted(window_numbers)}")
        i += 1

    return solution


numbers = [
    [1, 2, 3, 5, 6],
    [4, 5, 6, 7, 8],
    [7, 8, 9, 1, 2]
]

print(f"Contains all digits from 1 to 9: {solution(numbers)}")