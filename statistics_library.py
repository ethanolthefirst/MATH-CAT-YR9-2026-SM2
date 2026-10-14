def mean(data):
    return sum(data) / len(data) if data else 0

def minimum(data):
    min_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
    return min_val

def maximum(data):
    max_val = data[0]
    for x in data:
        if x > max_val:
            max_val = x
    return max_val

def range_val(data):
    return maximum(data) - minimum(data)

    def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    else:
        return sorted_data[mid]

def lower_quartile(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    # Use lower half of dataset
    lower_half = sorted_data[:mid]
    return median(lower_half)

def upper_quartile(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    # Use upper half of dataset
    if n % 2 == 0:
        upper_half = sorted_data[mid:]
    else:
        upper_half = sorted_data[mid + 1:]
    return median(upper_half)

def interquartile_range(data):
    return upper_quartile(data) - lower_quartile(data)

def variance(data):
    m = mean(data)
    # Population variance
    return sum((x - m) ** 2 for x in data) / len(data)

def standard_deviation(data):
    return variance(data) ** 0.5