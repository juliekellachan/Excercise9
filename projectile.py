from math import pi, tan, cos

g = 9.81
v = 44
y = 1
x = 0.5
t = 80 * (pi/180)

top = x * x * g
print (top)
bottom = v * cos(t) * cos(t) * v * 2
print ()
fraction = top / bottom

xtan0 = x * tan (t)
print (xtan0)

height = y + (xtan0) - fraction

print(height)


















