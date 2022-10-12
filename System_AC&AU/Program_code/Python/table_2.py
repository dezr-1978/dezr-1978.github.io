import pypyodbc
from prettytable import PrettyTable  # Импортируем установленный модуль.

mySQLServer = "GASE-PK"
myDatabase = "MAGISTER"
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase +';')
cursor = connection.cursor()
mySQLQuery = ("""
                SELECT TOP 1000 [id] ,[id_prod], [name_prod], [od_vymiru], 			
                [cina],[kod_operac], [vhid_zal_kilkst], [vhid_zal_suma], 				
                [nadishlo_kilkist] ,[nadishlo_suma], [vybulo_kilkist] ,					
                [vybulo_suma] ,[zalysho_kilkist] ,[zalyshok_suma]	
                            FROM [Magister].[dbo].[Mashinograma_OTP_5]
                              """)
cursor.execute(mySQLQuery)
results = cursor.fetchall()

for row in results:
    id = row[0]
    id_prod = row[1]
    name_prod = row[2]
    od_vymiru = row[3]
    cina = row[4]
    kod_operac = row[5]
    vhid_zal_kilkst = row[6]
    vhid_zal_suma = row[7]
    nadishlo_kilkist = row[8]
    nadishlo_suma = row[9]
    vybulo_kilkist = row[10]
    vybulo_suma = row[11]
    zalysho_kilkist = row[12]
    zalyshok_suma = row[13]

    th = ['id', 'id_prod', 'name_prod', 'od_vymiru', 'cina', 'kod_operac', 'vhid_zal_kilkst', 'vhid_zal_suma',
          'nadishlo_kilkist', 'nadishlo_suma', 'vybulo_kilkist', 'vybulo_suma', 'zalysho_kilkist', 'zalyshok_suma']
    td = (str(id), str(id_prod), str(name_prod),  str(od_vymiru), str(cina), str(kod_operac), str(vhid_zal_kilkst), str(vhid_zal_suma)
           , str(nadishlo_kilkist), str(nadishlo_suma), str(vybulo_kilkist), str(vybulo_suma), str(zalysho_kilkist), str(zalyshok_suma))

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
    
connection.close()
