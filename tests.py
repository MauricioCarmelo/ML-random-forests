import math

x = 3/float(4)
y = 1/float(4)

result = - x*(math.log(x, 2)) - y*(math.log(y, 2))

u = 2/float(3)
v = 1/float(3)

gain = -u*(math.log(u, 2)) - v*(math.log(v, 2))
gain = (3/float(4)) * gain

print result - gain