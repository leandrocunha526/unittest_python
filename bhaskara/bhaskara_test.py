def bhaskara_test(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta >= 0:
        x1 = (-b + delta ** (1/2)) / (2 * a)
        x2 = (-b - delta ** (1/2)) / (2 * a)
        return x1, x2
    else:
        return None
