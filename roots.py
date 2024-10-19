#input--a=1
   #    b=-3
    #   c=2
#Output:     Roots:(2.0,1.0)
a=int(input("give a value: "))
b=int(input("give b value: "))
c=int(input("give c value: "))
d1=(b**2-4*a*c)*0.5
d2=(b**2-4*a*c)*0.5
d=(b**2)-4*a*c
root1=(-b+(d**(0.5)))/2*a
root2=(-b-(d**(0.5)))/2*a
print(f"Roots: ",({root1},{root2}))
