import mysql.connector

#ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
connection = mysql.connector.connect(
host ="localhost",
user ="root",
password="password",
database="customer",
)

# print(connection)

db_cursor = connection.cursor()

#สร้าง String ไว้รอใส่คำสั่งสำหรับการ SELECT
db_cursor.execute("SELECT * FROM user")

#ดึงข้อมูลมาเก็บไว้ใน result
result = db_cursor.fetchall()

#แสดงผลข้อมูลมาทีละตัวจากที่ SELECT ได้ทั้งหมด
for data in result:
  print(data)