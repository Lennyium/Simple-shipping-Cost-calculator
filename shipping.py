#Weight in pounds(lb)
weight = 41.5

#Ground shipping
if weight < 2:
  cost = weight * 1.50 + 20
  print("Ground shipping cost is: ", cost)
elif weight > 2 and weight <= 6:
  cost = weight * 3.00 + 20
  print("Ground shipping cost is: ", cost)
elif weight > 6 and weight <=10:
  cost = weight * 4.00+ 20
  print("Ground shipping cost is: ", cost)
else:
  cost = weight * 4.75 + 20
  print("Ground shipping cost is: ", cost)

#Cost of Ground shipping premium
ground_shipping_premium = 125
print("Ground shipping premium cost is: ", ground_shipping_premium)

#Drone shipping
if weight < 2:
  cost = weight * 4.50
  print("Drone shipping cost is: ", cost)
elif weight > 2 and weight <= 6:
  cost = weight * 9.00
  print("Drone shipping cost is: ", cost)
elif weight > 6 and weight <=10:
  cost = weight * 12.00
  print("Drone shipping cost is: ", cost)
else:
  cost = weight * 14.25
  print("Drone shipping cost is: ", cost)
