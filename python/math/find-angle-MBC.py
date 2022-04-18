import math

ab,bc = input().split()
ab,bc = int(ab),int(bc)

print(str(int(round(math.degrees(math.atan2(ab,bc))))), end = '°')