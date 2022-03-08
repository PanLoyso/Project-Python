def personal_data(name, lastname, year_of_birth, city, email, phone):
    print(f"имя: {name}, фамилия: {lastname}, Год рождения: {year_of_birth}, город проживания: {city}, email: {email}, телефон: {phone}")
personal_data(
    name = input("Введите имя: "),
    lastname = input("Введите фамилию: "),
    year_of_birth = input("Введите год рождения: "),
    city = input("Введите город проживания: "),
    email = input("Введите email: "),
    phone = input("Введите номер телефона: ")
)