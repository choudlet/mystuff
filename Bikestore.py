class Bicycle(object):
	def __init__(self, brand, weight, cost):
		self.weight = weight
		self.cost = cost
		self.brand = brand
		

B1 = Bicycle("Cannondale", 45, 300),
B2 = Bicycle("Schwinn", 70, 120),
B3 = Bicycle("Mongoose", 34, 1000),
B4 = Bicycle("Cheapo", 65, 250),
B5 = Bicycle("Premier", 40, 600),
B6 = Bicycle("Speciality", 55, 450),

bikes = [B1, B2, B3, B4, B5, B6]
	
class Customer(object):
	
	def __init__(self, name, funds, bikes_owned):
		self.funds = funds
		self.bikes_owned = bikes_owned
		self.name = name
		pass
	
def wantbike():
	for Customer in Customers:
		if Customer.bikes_owned == 0:
			print (" {} needs a bike today.".format(Customer.name))
	pass
C1 = Customer("David", 1000, 0)
C2 = Customer("Tracy", 600, 0)
C3 = Customer("Michelle", 400, 0)
C4 = Customer("Rick", 2000, 2)

Customers = [C1, C2, C3, C4]

class Bikeshop(object):
	def __init__(self, name):
		self.name = name
		self.inventory = []
		self.money = 0
	def add_bikes(self, bikes):
    		if instance(bikes, Bycicle):
        		self.inventory.append(bikes)
BS1 = Bikeshop("Pat's Bikes")
BS2 = Bikeshop("City Bikes")
BS3 = Bikeshop("Slick Bikes")

Bikeshops = [BS1, BS2, BS3]


if __name__ == "__main__":
	wantbike()
	add_bikes()