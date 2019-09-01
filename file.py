nuber_of_pizzas = eval(input("Сколько пицц вы хотите? "))
cost_per_pizza = eval(input("Сколько стоит пицца? "))
subtotal = nuber_of_pizzas * cost_per_pizza
tax_rate = 0.08
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax
print("Полная стоимость $",total
print("В том числе $", subtotal, " за пиццу и")
print("$", sales_tax, "налог с продаж")    
