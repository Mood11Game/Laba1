list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

index_mid=len(list_players)//2 #индекс середины массива

first=list_players[:index_mid] #Первая команда
second=list_players[index_mid:] #Вторая команда

print(first)
print(second)