import sqlite3

connect = sqlite3.connect("customers.db")

def create_table():
    connect.execute("CREATE TABLE IF NOT EXISTS customers (name TEXT , surname TEXT, id TEXT, password TEXT )")
create_table()

def addCustomers(name,surname,id,password):
    connect.execute(f"""insert into customers
                    (name,surname,id,password)
                    values('{name}','{surname}','{id}','{password}')""")

# addCustomers("Berkant","Zor",11347318604,135790)
# addCustomers("Özlem","Şen",31201006430,745248)
# addCustomers("Emre","Zor",1234578901,123456)
# addCustomers("Elif","Zor",1098765432,654321)


cursor = [row for row in connect.execute("select * from customers")]

# def update(id):
#         connect.execute("update  customers set id = ? where name = 'ALİ'",(id,))
# update()
 
 
print(cursor)

    
    
connect.commit()
connect.close()