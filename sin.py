import math
import os

os.system('color 0a')
os.system('mode 1000')

o = int(input("Me de um angulo em graus e direi - te o seno : "))
x = math.radians(o)
y = math.sin(x)

if math.isclose(y, 0, rel_tol=1e-9, abs_tol=1e-14) == True:
    print('0')
else:
    print(y)
input('fim')
