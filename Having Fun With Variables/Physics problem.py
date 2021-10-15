#A stone is dropped into a deep well and is heard to hit the water 3.41 s after being dropped.
#Determine the depth of the well.
import constant
T = 3.41 #seconds
a = constant.GRAVITY
Vi = 0
d = Vi*T + .5*a*(T**2)
print(d)