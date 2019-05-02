import math
from Bootstrap import *
import pandas as pd
"""
x = 3/float(4)
y = 1/float(4)

result = - x*(math.log(x, 2)) - y*(math.log(y, 2))

u = 2/float(3)
v = 1/float(3)

gain = -u*(math.log(u, 2)) - v*(math.log(v, 2))
gain = (3/float(4)) * gain

print result - gain
"""

dataframe = pd.read_csv("data/input_data3.csv")

bootstrap = Bootstrap()
bootstrap.generate(dataframe)

print "training set"
print bootstrap.get_training_set()

print "test set"
print bootstrap.get_test_set()



