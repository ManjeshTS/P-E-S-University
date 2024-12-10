mass_D=1
mass_E=5
ratio_A=input("Enter the ratio used by A : ")
ratio_B=input("Enter the ratio used by B : ")

a,b=ratio_A.split(":")
c,d=ratio_B.split(":")
a,b=int(a),int(b)
c,d=int(c),int(d)

print("mass of Compound(A) =", a*1+b*5)
print("Mass of Compound(B) =", c*1+d*5)