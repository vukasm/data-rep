import mysql.connector
import dbconfig as cfg

db=mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor=db.cursor()
sql="CREATE TABLE chocolates (id INT AUTO_INCREMENT PRIMARY KEY, brand VARCHAR(250), kind VARCHAR(250), price FLOAT)"

cursor.execute(sql)

db.commit()