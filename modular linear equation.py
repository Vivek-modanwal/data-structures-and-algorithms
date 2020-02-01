# ax congruent to b(mod n)
# find the values of x,if multiplied by a
# and divided by n leaves remainder of b

# if b=1 and a and n relatively prime
# then modular_equation(a,1,n) give 
# modular multiplicative inverse of a
def modular_equation(a,b,n):
	d,x,y=extended_Euclid(a,n)
	L=[]
	if b%d==0:
		_x=(x*(b//d))%n
		for i in range(d):
			L.append((_x+i*(n//d))%n)
	return L

# extended euclid's GCD algorithm
def extended_Euclid(a,b):
	if b==0:
		return a,1,0
	d,x,y=extended_Euclid(b,a%b)
	return d,y,x-(a//b)*y


print(modular_equation(35,10,50))