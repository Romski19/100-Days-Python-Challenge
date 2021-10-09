def largest_difference(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    result = largest - smallest
    return result
largest_difference([22, 19, 58])