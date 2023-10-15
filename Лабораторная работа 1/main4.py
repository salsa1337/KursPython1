users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
stats = {"Общее количество": 0, "Уникальные посещения": 0}
stats["Общее количество"] = len(users)
unique_users = set(users)
stats["Уникальные посещения"] = len(unique_users)
print(stats)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
