# bounce.py
#
# Exercise 1.5

current_height = 100

for i in range(1, 11):
    current_height = round(current_height * (3.0 / 5.0), 4)
    print(f'{i}: {current_height}')
