age = int(input("Введите возраст человека: "))

people_data1 = {"Дмитрий": 34, "Антон": 27, "Леонид": 63, "Игорь": 26, "Андрей": 43, "Владимир": 71, "Анатолий": 34, "Павел": 37, "Илья": 62, "Александр": 19}
people_data2 = {"Евгения": 56, "Юлия": 31, "Екатерина": 43, "Ирина": 23, "Полина": 24, "Мария": 29, "Наталья": 23, "Анна": 46, "Валерия": 31, "Кристина": 20}
matching_people = []

for person, person_age in people_data1.items():
    if person_age == age:
        matching_people.append(person)

for person, person_age in people_data2.items():
    if person_age == age:
        matching_people.append(person)

if len(matching_people) > 0:
    print("Люди с возрастом", age, ":", matching_people)
else:
    print("Нет людей с возрастом", age)