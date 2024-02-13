def square(radius_square):
   pe = 3.14
   areas = []

   for i in radius_square:
      areas.append(pe * i)
   return areas


radius = [12,35,4]
print(square(radius))
