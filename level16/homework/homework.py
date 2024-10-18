def print_range(start, end):
    for number in range(start, end + 1):
        print(number)

# მაგალითი
print_range(1, 10)

def student_info(name, surname, age, academy):
    print(f"My name is {name}, my surname is {surname}, I study in {academy}.")

# მაგალითი
student_info("გიორგი", "მოძღვრიშვილი", 20, "საქართველოს ტექნიკური უნივერსიტეტი")

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# მაგალითი
greet("გიორგი", "მოძღვრიშვილი")

def sum_two_numbers(a, b):
    return a + b

# დაბრუნებული მნიშვნელობა ცვლადში
result_sum = sum_two_numbers(5, 10)
print(result_sum)


def multiply_three_numbers(a, b, c):
    return a * b * c

# დაბრუნებული მნიშვნელობა ცვლადში
result_product = multiply_three_numbers(2, 3, 4)
print(result_product)
6. 

def print_food_list(food_list):
    for food in food_list:
        print(food)

# მაგალითი
foods = ["პიცა", "ჰამბურგერი", "სალათი"]
print_food_list(foods)