from flask import Flask
from flask import request
app = Flask(__name__)
import mysql.connector

#ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
connection = mysql.connector.connect(
host ="localhost",
user ="root",
password="password",
database="customer",
)
db_cursor = connection.cursor()
@app.route('/login', methods=['POST'])
def login():
    
    content = request.json
    username= content['username']
    password= content['password']
    # print(username)
    # print(password)
    
    db_cursor.execute("SELECT * FROM customer.user ")
    results = db_cursor.fetchall()
    
    for result in results :     
        
        if username == result[1] and password == result[2]:
             
             return("success")
         
               
    return("not found")    
# @app.route('/login', methods=['POST'])
# def login():
    
#     content = request.json
#     username= content['username']
#     password= content['password']
#     print(username)
#     print(password)
    
#     #สร้าง String ไว้รอใส่คำสั่งสำหรับการ SELECT
#     db_cursor.execute("SELECT * FROM customer.user WHERE username = '" +username+ "' AND password ='"+password+"'")
#     #ดึงข้อมูลมาเก็บไว้ใน result
#     result = db_cursor.fetchall()
#     size = len(result)
#     for i in size :
#         if   == 0 :
#             print ('not found')
#         elif i == 1 :
#             print ('success')    
            

    
    # result = db_cursor.fetchall()
    # size = len(result)
    # for results in result:
    #     if result == 
        



# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/users",methods=['GET'])
# def getusers():
#     #สร้าง String ไว้รอใส่คำสั่งสำหรับการ SELECT
#     db_cursor.execute("SELECT * FROM user")
# #ดึงข้อมูลมาเก็บไว้ใน result
#     result = db_cursor.fetchall()
#     return result



             
             
         

       
            
    
    
    
    
    
    
    

    
    
    
    

    
    
    
  
    

    
    