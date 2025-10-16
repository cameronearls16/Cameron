foods = ["pizza", "tacos", "sushi", "pasta", "ice cream"]

print(foods[1])
print(foods[-1])

foods.append("ramen")
foods.insert(0, "apple")
del foods[2]

print(len(foods))

for food in foods:
    print(food.upper())

ends = [foods[0], foods[-1]]
print(ends)

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

numbers = list(range(21))

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    return lst[::-1][::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(lst):
    total = 0
    for row in lst:
        total += sum(row)
    return total

print(sum_nested(numbers))

def make_grid():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid

def replace_multiples_of_3(lst):
    new_lst = []
    for row in lst:
        new_row = []
        for item in row:
            if item % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(item)
        new_lst.append(new_row)
    return new_lst

def sum_not_question(lst):
    total = 0
    for row in lst:
        for item in row:
            if item != "?":
                total += item
    return total

grid = make_grid()
updated = replace_multiples_of_3(grid)
result = sum_not_question(updated)

print(grid)
print(updated)
print(result)

def make_grid():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid

def replace_multiples_of_3(lst):
    new_lst = []
    for row in lst:
        new_row = []
        for item in row:
            if item % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(item)
        new_lst.append(new_row)
    return new_lst

def sum_not_question(lst):
    total = 0
    for row in lst:
        for item in row:
            if item != "?":
                total += item
    return total

grid = make_grid()
updated = replace_multiples_of_3(grid)
result = sum_not_question(updated)

print(grid)
print(updated)
print(result)

print(get_every_5th([1, 4, 5, 6, 7, 8, 4, 3, 4, 5, 6, 3, 8, 8, 9]))
