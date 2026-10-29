def second_largest(numbers):
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        return None
    
    unique_numbers.sort()
    
    return unique_numbers[-2]

print(second_largest([10, 5, 8, 10, 3]))
print(second_largest([4, 4, 4]))
print(second_largest([-5, -2, -8, -3]))