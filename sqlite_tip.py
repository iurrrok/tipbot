import sqlite3
#файл для работы с бд

#создаем таблицу  и файл в бд
def tip_table(file):
	conn = sqlite3.connect(file)
	c = conn.cursor()
	c.execute('''CREATE TABLE tipbot(id,wallet,nickname,bal,bal2)''')
	conn.commit()
	conn.close()

#сохраняем в файл
def tip_save (id,wallet,nickname,bal,bal2):
	conn = sqlite3.connect(file)
	c = conn.cursor()
	
	tipbot = [(id,wallet,nickname,bal,bal2)]
	c.executemany("INSERT INTO tipbot VALUES (?,?,?,?,?)", tipbot)
	conn.commit()
	conn.close()

#чтение всего файла
def tip_read (file):
	conn = sqlite3.connect(file)
	#conn.row_factory = sqlite3.Row
	cursor = conn.cursor()
	print("Here's a listing of all the records in the table:")
	for row in cursor.execute("SELECT rowid, * FROM tipbot ORDER BY id"):
		print(row)
#	cursor.execute(sql)
#	print(cursor.fetchall())
	conn.close()

#поик по ключам
def tip_find(file,data):
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
	for row in cursor.execute("SELECT rowid, * FROM tipbot ORDER BY id"):
		for i in row:
			if i == data:
				return(i)
				break
			else:
				continue
	conn.close()

#поиск номер 2
def tip_find1(file,datas,data):
	'''
	'''
	conn = sqlite3.connect(file)
	#conn.row_factory = sqlite3.Row
	cursor = conn.cursor()
	#print(f"dates={datas}, data={data}")
	sql = f"SELECT * FROM tipbot WHERE {datas}={data} "
	cursor.execute(sql)
	return(cursor.fetchone())
	#print(cursor.fetchone())
	conn.close()
	
def tip_find_row(file,data):
	''' возвращает:
	(4, , '', '', '25', '10') либо None
	'''
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
	for row in cursor.execute("SELECT rowid, * FROM tipbot ORDER BY id"):
		for i in row:
			if i == data:
				return(row)
				break
			else:
				continue
	conn.close()
	
	
#редактирование н1(не пашет)
def tip_edit(file,dataid,datacolumn):
	sqlite_file = file
	table_name = 'tipbot'
	id_column = dataid
	column_name = datacolumn
	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	# A) Inserts an ID with a specific value in a second column
	try:
		c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".format(tn=table_name, idf=id_column, cn=column_name))
	except sqlite3.IntegrityError:
		print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
	conn.commit()
	conn.close()
	

def tip_edit1(file,dataidc,datacn):
	sqlite_file = file
	table_name = 'tipbot'
	id_column = dataidc
	column_name = datacn
	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	# B) Tries to insert an ID (if it does not exist yet)
	# with a specific value in a second column
	c = conn.cursor()
	c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".format(tn=table_name, idf=id_column, cn=column_name))
	conn.commit()
	conn.close()

def tip_edit2(file,datacn1,data1,datacn2,data2):
	sqlite_file = file
	table_name = 'tipbot'
	column_name1 = datacn1
	column_name2 = datacn2
	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	# C) Updates the newly inserted or pre-existing entry
	c.execute("UPDATE {tn} SET {cn2}='{d2}' WHERE {cn1} = '{d1}' ".format(tn=table_name, cn1=column_name1,d1=data1,d2=data2,cn2=column_name2))
	conn.commit()
	conn.close()
#редактирование ,пашет
def tip_edit3(file,col2,data2,col1,data1):
	'''
	кол/данные,которые надо поменять
	кот надо найти
	'''
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
	sql = f"UPDATE tipbot SET {col1} = '{data1}' WHERE {col2}='{data2}' "
	cursor.execute(sql)
	conn.commit()
	
#удаление всей строки по флагу
def tip_del(file,col,data):
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
	sql = f"DELETE FROM tipbot WHERE {col} = '{data}' "
	cursor.execute(sql)
	conn.commit()

	


#тестовый стенд
#tip_save('sqlite_tip_test.db',555555,'hdhuug','Lara',-1,+99)
#tip_table('sqlite_tip_test.db')
#tip_read('sqlite_tip_test.db')
#tip_find('sqlite_tip_test.db','Emgeldea')
#tip_find1('sqlite_tip_test.db','id','657255765')
#tip_find_row('sqlite_tip_test.db','Emelea')
#tip_edit2('sqlite_tip_test.db','nickname','pspdimiiiarik','bal2','3')
#tip_edit3('sqlite_tip_test.db','nickname','Lara','bal2','100')
#tip_del('sqlite_tip_test.db','nickname','Vasea')

#g=tip_find1('sqlite_tip_test.db','id','657255765')
#g=tip_find_row('sqlite_tip_test.db','Emyecdleda')
#if g == None:
#	print('oh shit')
