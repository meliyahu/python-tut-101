f = open('data.txt')
fruits = f.read()
fruits = fruits.splitlines()
print("Fruits:")
for fruit in fruits:
    print(fruit)