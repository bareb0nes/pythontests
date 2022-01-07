def approx_equals(a, b):
    difference = a - b
    if abs(difference) < 0.001:
        return True
    else:
        return False
