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