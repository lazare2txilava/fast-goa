# 2) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.
# a = 7
# b = 15
# print("a და b-ის ჯამი:", a + b)

# 3) შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია.
# კომენტარი: სტრინგების შეერთება (კონკატენაცია) ნიშნავს მათ შეერთებას ერთად.
# str1 = "გამარჯობა"
# str2 = "მეგობარო"
# print("კონკატენაცია:", str1 + " " + str2)

# 4) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი.
# x = 10
# y = 3
# print("x და y-ის განაყოფი:", x / y)  # მიიღება float, რადგან division ოპერაცია implicit convert-ს აკეთებს int-დან float-ში.

# 5) შედარების ოპერატორები:
# print(10 == 10)   # True - ტოლობა
# print(5 != 3)     # True - უთანასწორობა
# print(7 > 4)      # True - მეტობა
# print(2 < 8)      # True - ნაკლებობა
# print(6 >= 6)     # True - მეტობა ან ტოლობა
# print(3 <= 7)     # True - ნაკლებობა ან ტოლობა

# 6) შედარების ოპერატორები და მათემატიკური ოპერაციები:
# print(5 + 5 == 8 + 2)  # True

# 7) ლოგიკური ოპერატორები:
# print(True and True)   # True
# print(True and False)  # False
# print(False and True)  # False
# print(False and False) # False

# print(True or True)    # True
# print(True or False)   # True
# print(False or True)   # True
# print(False or False)  # False

# 8) ლოგიკური და შედარების ოპერატორები:
# print(5 > 2 and 3 < 4)   # True
# print(10 == 10 or 5 > 8)  # True
# print(7 != 5 and 9 > 6)   # True
# print(3 >= 2 or 4 == 5)   # True
# print(not (5 == 5))       # False

# 9) for loop 1-დან 10-მდე რიცხვების დასაბეჭდად:
# for i in range(1, 11):
#     print(i)

# 10) list-ის რიცხვების ჯამის გამოსათვლელად:
# numbers = [1, 2, 3, 4, 5]
# total_sum = 0
# for num in numbers:
#     total_sum += num
# print("სიაში არსებული რიცხვების ჯამი:", total_sum)
# 11) for loop თითოეული სიმბოლოს დასაბეჭდად სტრინგში:
# string = "Hello, World!"
# for char in string:
#     print(char)

# 12) while loop 1-დან 10-მდე რიცხვების დასაბეჭდად:
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# 13) while loop რომელიც გამოტოვებს რიცხვებს 50-დან 60-მდე:
# i = 1
# while i <= 100:
#     if 50 <= i <= 60:
#         i += 1
#         continue
#     print(i)
#     i += 1

# 14) while loop რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს:
# i = 1
# total = 0
# while total < 50:
#     total += i
#     i += 1
# print("რიცხვების ჯამი, რომელიც უდრის ან მეტია 50-ს:", total)

# 15) ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაპრინტავს თუ იყოფა 3-ზე ან 5-ზე:
# def check_divisibility(num):
#     if num % 3 == 0 and num % 5 == 0:
#         print(f"{num} იყოფა როგორც 3-ზე, ისე 5-ზე.")
#     elif num % 3 == 0:
#         print(f"{num} იყოფა 3-ზე.")
#     elif num % 5 == 0:
#         print(f"{num} იყოფა 5-ზე.")
#     else:
#         print(f"{num} არ იყოფა 3-ზე ან 5-ზე.")

# number = int(input("შეიყვანეთ რიცხვი: "))
# check_divisibility(number)
# 16) ფუნქცია რომელიც გამოთვლის სიაში რიცხვების საშუალო არითმეტიკულს:
# def calculate_average(numbers_list):
#     return sum(numbers_list) / len(numbers_list)

# numbers_list = [1, 3, 4, 5, 2]
# print("საშუალო არითმეტიკული:", calculate_average(numbers_list))

# 17) ფუნქცია რომელიც ყოველი მეორე ასოს uppercase-ში აქცევს:
# def alternate_uppercase(string):
#     result = ""
#     for i in range(len(string)):
#         if i % 2 == 0:
#             result += string[i].upper()
#         else:
#             result += string[i].lower()
#     return result

# test_string = "hello"
# print("მოდიფიცირებული სტრინგი:", alternate_uppercase(test_string))

# 18) ფუნქცია რომელიც აბრუნებს სიას, სადაც რიცხვების კვადრატებია:
# def square_numbers(numbers_list):
#     squared_list = []
#     for num in numbers_list:
#         squared_list.append(num ** 2)
#     return squared_list


# numbers_list = [3, 12, 5, 2, 6]
# print("რიცხვების კვადრატები:", square_numbers(numbers_list))

# 19) გატესტეთ ყველა ფუნქცია/მეთოდი ზემოთ მოყვანილი მაგალითებით.