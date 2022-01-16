# 导入MySQL驱动
import mysql.connector

conn = mysql.connector.connect(user='root',password='12345',database='pyqt')
cursor = conn.cursor()
cursor.execute('SELECT * FROM student')
values = cursor.fetchall()
print(values)

