# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then add a new pizza to the original list, add a different pizza to the list friend_pizzas, and prove that you have two seperate lists by printing them both.

pizzas = ['Cheese', 'Pepperoni', 'Mushrooms and Olives']

friend_pizzas = pizzas[:]

pizzas.append('Tomato')
friend_pizzas.append('Hawaiian')

print("My favorite pizzas are: ")

for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")

for pizza in friend_pizzas:
    print(pizza)