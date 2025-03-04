def to_p_adic(n, p):
    """Konvertiert eine Dezimalzahl in eine p-adische Zahl."""
    result = ''
    while n > 0:
        result = str(n % p) + result
        n //= p
    return result if result else '0'

def from_p_adic(p_adic, p):
    """Konvertiert eine p-adische Zahl in eine Dezimalzahl."""
    decimal = 0
    for i, digit in enumerate(reversed(str(p_adic))):
        decimal += int(digit) * (p ** i)
    return decimal

def add_p_adic(a, b, p):
    """Addiert zwei p-adische Zahlen."""
    a_decimal = from_p_adic(a, p)
    b_decimal = from_p_adic(b, p)
    result_decimal = a_decimal + b_decimal
    return to_p_adic(result_decimal, p)

def subtract_p_adic(a, b, p):
    """Subtrahiert zwei p-adische Zahlen."""
    a_decimal = from_p_adic(a, p)
    b_decimal = from_p_adic(b, p)
    result_decimal = a_decimal - b_decimal
    return to_p_adic(result_decimal, p)

# Beispielanwendung:
p = 5
x = 12
y = 23

x_p_adic = to_p_adic(x, p)
y_p_adic = to_p_adic(y, p)

print(f"{x} in {p}-adischer Darstellung: {x_p_adic}")
print(f"{y} in {p}-adischer Darstellung: {y_p_adic}")

sum_p_adic = add_p_adic(x_p_adic, y_p_adic, p)
difference_p_adic = subtract_p_adic(x_p_adic, y_p_adic, p)

print(f"{x} + {y} in {p}-adischer Darstellung: {sum_p_adic}")
print(f"{x} - {y} in {p}-adischer Darstellung: {difference_p_adic}")
