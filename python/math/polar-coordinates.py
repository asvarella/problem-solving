import cmath

z = input()
z = complex(z)
r,p = cmath.polar(z)
print(f'{r}\n{p}')