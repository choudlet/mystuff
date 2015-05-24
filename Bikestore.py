
import random

#this simply prints all customers that want to buy a bike
def wantbike():
	for Customer in Customers:
		if Customer.bikes_owned == 0:
			print (" {} needs a bike today.".format(Customer.name))

#building the blueprint for the bicycle object
class Bicycle(object):
	def __init__(self, brand, weight, cost):
		self.weight = weight
		self.cost = cost
		self.brand = brand
        def display(self):
        	print (" {} (Weight:{} Cost:{})".format(self.brand, self.weight, self.cost))

#building the blueprint for the customer object			
class Customer(object):
	def __init__(self, name, funds, bikes_owned):
		self.boughtbike = []
		self.funds = funds
		self.bikes_owned = bikes_owned
		self.name = name
		def display(boughtbike):
        		print(" {} ".format(self.brand))
		pass

	def ownbike(self, bike):
		self.boughtbike.append(bike)
    		self.funds = self.funds - bike.cost
    	
def buybike():
	purchasestore = random.choice(Bikeshops)
	for Customer in Customers:
		if Customer.bikes_owned == 0:
			for bike in purchasestore.inventory:
				if bike.cost <= Customer.funds:
					Customer.ownbike(bike)
			for bike in Customer.boughtbike:
				bike_display = (" {} (Weight:{} Cost:{})".format(bike.brand, bike.weight, bike.cost))
			print "Today %s Bought This Bike(s) %s and has %s Money Left" % (Customer.name, bike_display, Customer.funds)
				
#building the blueprint for the bikeshop object
class Bikeshop(object):
	def __init__(self, name, margin):
		self.name = name
		self.inventory = []
		self.money = 100000
		self.margin = margin

	def add_bike(self, bike):
		self.inventory.append(bike)
                self.money = self.money - bike.cost
	


def fillBikeShops():
	for shop in Bikeshops:
		howMany = random.randint(2,15)
		for i in range(2,howMany):
			aBike = random.choice(bikes)
			shop.add_bike(Bicycle(aBike.brand, aBike.weight, aBike.cost))

def show_prices():
	for shop in Bikeshops:
		for bike in shop.inventory:
				bike.cost = bike.cost * shop.margin
		print "%s has all these great bikes in stock today:" % (shop.name)
                for bike in shop.inventory:
                  bike.display()


if __name__ == "__main__":
	B1 = Bicycle("Cannondale", 45, 300)
B2 = Bicycle("Schwinn", 70, 120)
B3 = Bicycle("Mongoose", 34, 1000)
B4 = Bicycle("Cheapo", 65, 250)
B5 = Bicycle("Premier", 40, 600)
B6 = Bicycle("Speciality", 55, 450)
bikes = [B1, B2, B3, B4, B5, B6]

C1 = Customer("David", 1000, 0)
C2 = Customer("Tracy", 600, 0)
C3 = Customer("Michelle", 400, 0)
C4 = Customer("Rick", 2000, 2)
Customers = [C1, C2, C3, C4]

BS1 = Bikeshop("Pat's Bikes", 1.2)
BS2 = Bikeshop("City Bikes", 1.6)
BS3 = Bikeshop("Slick Bikes", 2.4)
Bikeshops = [BS1, BS2, BS3]

wantbike() #Represents who wants to buy (David, Tracy, Michelle)
fillBikeShops()
show_prices()
buybike()