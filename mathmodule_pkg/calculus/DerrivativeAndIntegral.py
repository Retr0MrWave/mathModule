def derrivative(f, dx):
    def fdot(x):
        return (f(x+dx)-f(x))/dx
    return fdot

def integral(f, x0, x1, dx):
    s = 0
    i = x0
    while i <= x1:
        s += f(i)*dx
        i += dx
    return s