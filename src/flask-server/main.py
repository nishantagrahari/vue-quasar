import psycopg2

hostname ='localhost'
database='Test'
username='postgres'
pwd='postgres'
port_id=5432

conn= None
cur= None


try:
        conn= psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )

        cur=conn.cursor()

        create_script =''' select * from public."Test_Table5" limit 10 '''    
        cur.execute(create_script)
        name=cur.fetchall()
        print(name)
        # (name)


   
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
   