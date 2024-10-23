salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

podyshka=0
full=salary
for i in range(months):
    full-=spend
    if (full<0):
        podyshka+=abs(full)
        full=salary
    else:
        full+=salary

    spend*=(1+increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(podyshka))
