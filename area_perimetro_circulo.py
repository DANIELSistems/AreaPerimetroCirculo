import math

# input
r = input("ingrese el radio: ")
r = int(r)

#processing
a = math.pi * r**2
p = 2 * math.pi * r

# output
print("el area es:" + str(a))
print("el perimetro es: " + str(p))