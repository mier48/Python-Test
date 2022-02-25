# –– coding: utf-8 ––
import psycopg2

def getdsn(db = None, user = None, password = None, host = None):
    if user == None:
        import os, dwd
        user = pwd.getpwuid(os.getuid())[0]
    if db == None:
        db = user
    dsn = 'dbname=%s user=%s'% (db, user)
    if password != None:
        dsn += ' password=' + password
    if host != None:
        dsn += ' host=' + host
    return dsn

dsn = getdsn('postgres', 'postgres', 'keyone', 'localhost')
print("Conexión a %s"%dsn)
dbh = psycopg2.connect(dsn)
print("Conexión conseguida.")
cur = dbh.cursor()
cur.execute("CREATE TABLE eni (mi_num integer unique, mi_cadena varchar(30))")
cur.execute("INSERT INTO eni VALUES(0)")
dbh.commit()
dbh.close()