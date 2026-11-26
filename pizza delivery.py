small_price = 8
large_price = 12
topping_price = 1
base_delivery = 2
base_delivery_miles = 5
extra_mile_fee = 1

print('Hello world!')

# Inputs
size = input("Kindly indicate `small` or `large`: ").lower()
topping = int(input('How many toppings: '))
radius_in_miles = int(input("How far do you live in miles?: "))

# Base cost
if size == 'small':
    base_cost = small_price
elif size == 'large':
    base_cost = large_price
else:
    print('Choose a size among the two')
    raise SystemExit

# Topping cost
topping_cost = topping_price * topping

# Delivery fee
if radius_in_miles == 0:
    delivery_fee = 0
elif radius_in_miles <= base_delivery_miles:
    delivery_fee = base_delivery
else:
    extra_miles = radius_in_miles - base_delivery_miles
    delivery_fee = base_delivery + extra_miles * extra_mile_fee

# Total cost
total_cost = base_cost + topping_cost + delivery_fee

print(f'The final cost is ${total_cost}')
