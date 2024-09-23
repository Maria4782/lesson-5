my_string = input("Введите название Вашего учебного заведения: ".upper())
print(my_string, "- отличный университет!".lower())
current_year = 2024
date_of_birth = input("В каком году вы родились?: ")
age = current_year - int(date_of_birth)
print("В этом году Вам: ".replace(' ', ''), age,  "года")
print(len(my_string))
print(my_string[0])
print(my_string[-1])

