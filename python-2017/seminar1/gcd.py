def calculate_gcd(a, b):
    return a if not b else calculate_gcd(b, a % b)
