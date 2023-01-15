import sqlalchemy as db
from sqlalchemy import engine,create_engine

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

def export_data2(comp_list):
    print(comp_list.head())
    engine = create_engine("mysql://root:1234@localhost/stock_store",echo = True)
    with engine.connect() as conn:
        comp_list.to_sql('company_list',con=conn,index=False,if_exists='append')