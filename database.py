import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='1234567')
        mycursor = conn.cursor()
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong, Please open MySQL app before running again: {str(e)}')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('''CREATE TABLE IF NOT EXISTS data (
                        ID VARCHAR(20),
                        Name VARCHAR(50),
                        Phone VARCHAR(15),
                        Role VARCHAR(50),
                        Gender VARCHAR(20),
                        Salary DECIMAL(10,2)
                    )''')

def insert(id, name, phone, role, gender, salary):
    try:
        mycursor.execute('INSERT INTO data (ID, Name, Phone, Role, Gender, Salary) VALUES (%s, %s, %s, %s, %s, %s)',
                         (id, name, phone, role, gender, salary))
        conn.commit()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to insert data: {str(e)}')

def id_exists(id):
    try:
        mycursor.execute('SELECT COUNT(*) FROM data WHERE ID=%s', (id,))
        result = mycursor.fetchone()
        return result[0] > 0
    except Exception as e:
        messagebox.showerror('Error', f'Error checking ID existence: {str(e)}')
        return False

def fetch_employees():
        mycursor.execute('SELECT* from data')
        result=mycursor.fetchall()
        return result


def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    conn.commit()

def search (option,value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()
connect_database()
