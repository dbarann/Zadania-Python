class Complex():
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	def __str__(self):
		return f"{self.real} i{self.imag}"
	
	def add(self,a):
		return Complex(self.real+a.real,self.imag+a.imag) 
		
	def subtract(self,a):
		return Complex(self.real-a.real,self.imag-a.imag)
		
	def multiply(self,a):
		return Complex((self.real*a.real-self.imag*a.imag),(self.real*a.imag+self.imag*a.real))
		
	def divide(self,a):
		return Complex(((self.real*a.real+self.imag*a.imag)/(float(a.real**2+a.imag**2))),((self.imag*a.real-self.real*a.imag)/(float(a.real**2+a.imag**20))))
		
	def abs(self):
		return (self.real**2+self.imag**2)**(0.5)
'''		
a = Complex(10,5)
b = Complex(1,1)

s = Complex.add(a,b)
print (s)
o = Complex.subtract(a,b)
print (o)
m = Complex.multiply(a,b)
print (m)
d = Complex.divide(a,b)
print (d)
ab = Complex.abs(a)
print (ab)
'''