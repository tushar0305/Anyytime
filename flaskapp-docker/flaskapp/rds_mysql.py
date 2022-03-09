import pymysql
conn = pymysql.connect(
        host= 'anyytime.cbh9no9tsabi.us-east-1.rds.amazonaws.com',
        port = 3306,
        user = 'admin',
        password = 'abhay234',
        db = 'anyytime'
        
    )

def insert_details(email):
    cur=conn.cursor()
    cur.execute("INSERT INTO annytime_data (email) VALUES (%s)", (email))
    conn.commit()