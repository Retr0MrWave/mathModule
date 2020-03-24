def gcd(a, b):
	if not(type(a) is int and type(b) is int):
		raise TypeError("Can't apply GCD/LCM to non-integer")
	if a == 0 and b == 0:
		raise ValueError("Arguments of GCD/LCM can't both be zeros")
	a = abs(a)
	b = abs(b)
	if a == 0 or b == 0:
		return a + b
	if a == b:
		return a
	if a == 1 or b == 1:
		return 1
	if a & 1 == 0 and b & 1 == 0:
		return 2 * gcd(a >> 1, b >> 1)
	if a & 1 == 0 and b & 1 != 0:
		return gcd(a >> 1, b)
	if a & 1 != 0 and b & 1 == 0:
		return gcd(a, b >> 1)
	if a & 1 != 0 and b & 1 != 0:
		if a > b:
			return gcd((a - b) >> 1, b)
		if a < b:
			return gcd((b - a) >> 1, a)

def lcm(a, b):
    return (a*b)//gcd(a, b)