

def export_data():
    

    try:
        import mysql.connector

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="stock_store",
            password="1234")

        print(mydb)


        if mydb.is_connected():
            print('connected')
        else:
            print('not connected')  
    except Exception as e:
        print('connection error : ',e)
    finally:
        mydb.close()
        print('now closed')