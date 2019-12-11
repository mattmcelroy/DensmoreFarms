# Curing recipe for black cod

#3/4 gallon brine is half my 6 quart buckets
# Full recipe from: 
# http://www.theoutdoorline.com/blog/post/2009/06/22/smoking-salmon-simplified.aspx

pounds = int(input("How many pounds (whole number) fish?: "))

def codcure(pounds):

	# determine number of 6 quart buckets of brine to make
	if pounds <= 0:
		print()
		print("No fish to smoke!")
		return
	elif pounds > 0 and pounds <= 6:
		buckets = 1
	elif pounds > 6 and pounds <= 12:
		buckets = 2
	elif pounds > 12 and pounds <= 18:
		buckets = 3
	elif pounds > 18 and pounds <= 24:
		buckets = 4
	print()
	print("{} buckets of brine".format(buckets))
 
	# Recipe per 6 quart bucket (3 quarts brine)
	# original recipe amount * (3/8)
	water = 2 * (3/8)
	sugar = 4 * (3/8)
	salt = 2 * (3/8)
	pepper = 2 * (3/8)
	bayleaves = 6 * (3/8)
	garlic = 1 * (3/8)
	
	print()
	print("Recipe per bucket")
	print("{} gallons warm water".format(water))
	print("{} cups brown sugar".format(sugar))
	print("{} cups kosher".format(salt))	
	print("{} tablespoons black pepper".format(pepper))
	print("{} bay leaves".format(bayleaves))
	print("{} tablespoons garlic powder".format(garlic))
	print()
	print("Total batch recipe")
	print("{} gallons warm water".format(water*buckets))
	print("{} cups brown sugar".format(sugar*buckets))
	print("{} cups kosher".format(salt*buckets))	
	print("{} tablespoons black pepper".format(pepper*buckets))
	print("{} bay leaves".format(bayleaves))
	print("{} tablespoons garlic powder".format(garlic*buckets))
	print()
	
# run the function to get the recipe
codcure(pounds)


