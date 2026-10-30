def longest_consecutive(numbers):
    if not numbers:
        return 0

        num_set = set(numbers)
        longest_streak = 0

        for num in num_set:

             if (num - 1) not in num_set:

    return longest_streak


print(longest_streak([100, 4, 200, 1, 3, 2]))


