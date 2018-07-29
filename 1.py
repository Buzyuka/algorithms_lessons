# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала для каждого предприятия. Программа должна определить среднюю
# прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

n = int(input("Введите количество предприятий: "))


def company__to_string(company):
    return f"{company.name} ({company.average_income})"


Company = namedtuple("Company", "name, incomes, average_income")
Company.__str__ = company__to_string

companies = []
all_incomes = []

for i in range(n):
    name = input(f"Введите наименование для пердприятия #{i+1}: ")
    incomes = input(f"Введите прибыль за 4 квартала для пердприятия разделенные запятой #{i+1}: ")
    incomes = list(map(int, incomes.split(",")))

    assert (len(incomes) == 4)

    average_income = sum(incomes) / 4
    all_incomes.extend(incomes)

    companies.append(Company(name, incomes, average_income))

average = sum(all_incomes) / len(all_incomes)

print()
print("Средняя прибыль:", average)
print("Предприятия с прибылью выше среднего:")
print(*filter(lambda x: x.average_income >= average, companies), sep="\n")

print("Предприятия с прибылью ниже среднего:")
print(*filter(lambda x: x.average_income < average, companies), sep="\n")
