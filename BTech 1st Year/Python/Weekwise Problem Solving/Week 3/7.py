l=int(input("Enter the length of the rectangular floor : "))
b=int(input("Enter the breadth of the rectangular floor : "))
a=int(input("Enter the side of the tile : "))
c=int(input("Enter the cost of one tile "))
area_tile=a*a
area_floor=l*b
la=int(input("Enter the labour charge : "))
print("The number of tiles required is = ", area_floor/area_tile)
print("The Total Cost  is = ", ((area_floor/area_tile)*c)+la)
