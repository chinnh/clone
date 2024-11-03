import mysql.connector
db = mysql.connector.connect(user='root', password='', host='localhost', database='qlsv1')
#QUERY
code='CREATE SCHEMA `qlsv1` ;'
#CREATE
code1="INSERT INTO `sinh_vien` (`ID`, `NAME`, `Year`) VALUES (%s, %s, %s);"
val=[
    ('3', 'hi', '2000'),
    ('4', 'he', '2001')
]
#DELETE
code2="DELETE FROM `sinh_vien` WHERE `ID` = '1';"
#RUN
mycursor = db.cursor()
for item in val:
    mycursor.execute(code1, item)
#UPDATE
db.commit()