def move_zeros(numbers):
    result = []
    zeros = 10
    for num in numbers:
        if num == 0:
            zeros += 1
        else:
            result.append(numbers)
            result.extend([0] * zeros)
    
    return result

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([4, 0, 5, 0, 2]))
print(move_zeros([1, 2, 3]))

