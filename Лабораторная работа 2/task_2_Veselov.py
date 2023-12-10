salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
spend_sum = spend # суммарные расходы в первый месяц
for i in range(months):
    spend_sum += spend * 1.03 ** i # рост суммарных расходов на величину трат с учетом роста цен
money_capital = spend_sum - salary * months # вычисление необходимой финансовой подушки
#В данном случае использование цикла с заданным числом шагов предпочтительнее
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))