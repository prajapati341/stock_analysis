
# with open('guru99.txt', 'a') as the_file:
#     the_file.write('Hello world \n')
#     print('hello world')


import logging 
import pandas as pd
import json
import sqlalchemy as db
from sqlalchemy import engine,create_engine
import pymysql
from sqlalchemy import MetaData,Table, Column, Integer, String,Float,DateTime
import warnings
import logging  
  




# def create_log():
#     logging.basicConfig(filename='logfile.log', level=logging.DEBUG, force=True)


def writeLog(get_output):
    logging.basicConfig(filename='logfile.log', level=logging.DEBUG, force=True)
    #logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)  
    logging.info(f'Log message {get_output}')  
    logging.warning(f'warning message {get_output}') 
    



def mysql_conn():
    try:
        with open('cred.json','r') as cred_file:
            cred=cred_file.read()

        obj=json.loads(cred)
        user=obj['user']
        pwd=obj['pwd']
        host=obj['host']
        database=obj['database']

        print('\n\n JSON file loaded')

    except Exception as json_file:
        print('credential file error ',json_file)
    
    try:
        
        pymysql.install_as_MySQLdb()
        engine = create_engine(f"mysql://{user}:{pwd}@{host}/{database}",echo = True)
        print('connected successful')
        str='connected'
        writeLog(str)
        return engine

    except Exception as conn_err:

        print('connection error :',conn_err)


def db_insert_company_list(connect_mysql):
    global comp_list

    comp_list=pd.read_excel('/home/sanjay/Stock_Analysis/working/company_list.xlsx')
    try:
       
        comp_list.to_sql('company_list',con=connect_mysql,index=False,if_exists='append')
            
        
    except Exception as e:
        print('db_insert_company_list > upload error > ',e)




def test2():
    print('hello world')


def main():
    #create_log()
     with warnings.catch_warnings():
        db_insert_company_list(mysql_conn().connect())   # calling mysql_conn() func than return "engine" than .connect()
        warnings.filterwarnings("ignore",category=DeprecationWarning)
    #print(comp_list.head())
    # print('hello world')

    
    #writeLog()

        
    

    
    
    
    



if __name__ == '__main__':
    main()
