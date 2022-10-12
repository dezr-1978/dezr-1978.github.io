from prettytable import PrettyTable  # Импортируем установленный модуль.

# Определяем твою шапку и данные.

th = ['MAC Address', 'IP Address', 'Mode', 'Rate (Mbps)', 'Signal (%)']
td = ['11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100',
      '11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100',
      '11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100',
      '11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100',
      '11:11:11:11:11:11', '192.168.0.103', '11n', '65', '100']
columns = len(th)  # Подсчитаем кол-во столбцов на будущее.

table = PrettyTable(th)  # Определяем таблицу.

# Cкопируем список td, на случай если он будет использоваться в коде дальше.
td_data = td[:]
# Входим в цикл который заполняет нашу таблицу.
# Цикл будет выполняться до тех пор пока у нас не кончатся данные
# для заполнения строк таблицы (список td_data).
while td_data:
    # Используя срез добавляем первые пять элементов в строку.
    # (columns = 5).
    table.add_row(td_data[:columns])
    # Используя срез переопределяем td_data так, чтобы он
    # больше не содержал первых 5 элементов.
    td_data = td_data[columns:]

print(table)  # Печатаем таблицу
