money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

c=1
full=money_capital
while (full>0):
    full -= spend
    if full<0:
        break
    full += salary
    spend*=(1+increase)
    c+=1

print("Количество месяцев, которое можно протянуть без долгов:", c)



