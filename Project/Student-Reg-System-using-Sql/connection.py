import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='Adnan@1521', database='webui')

if conn.is_connected():
    print('connection established')
print(conn)
print(conn.is_connected())



cursor = conn.cursor()

cursor.execute("""
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id VARCHAR(20),
    name VARCHAR(100),
    mobile VARCHAR(15),
    salary FLOAT
)
""")

print("Table created successfully.")
conn.close()
