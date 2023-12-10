list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_index = len(list_players)//2 # делим игроков на две команды
team_1 = list_players[:middle_index]# команда 1
team_2 = list_players[middle_index:]# команда 2
print("Всего игроков:", len(list_players))
print("Команда 1:", team_1)
print("Команда 2:", team_2)
