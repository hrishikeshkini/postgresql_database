import psycopg2 as pg

def create_table():
    conn = pg.connect("dbname = 'data2' user = 'postgres' password = 'postgres' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()


def insert(roll, name, marks):
    conn = pg.connect("dbname = 'data2' user = 'postgres' password = 'postgres' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)", (roll, name, marks))
    conn.commit()
    conn.close()

def view():
    conn = pg.connect("dbname = 'data2' user = 'postgres' password = 'postgres' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(roll):
    conn = pg.connect("dbname = 'data2' user = 'postgres' password = 'postgres' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=%s", (roll,))
    conn.commit()
    conn.close()


def update(roll, name, marks):
    conn = pg.connect("dbname = 'data2' user = 'postgres' password = 'postgres' port = '5432' host = 'localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=%s, marks=%s WHERE rollno=%s",(name,marks,roll))
    conn.commit()
    conn.close()

# create_table()
# insert(2,'hrishikesh',100)
# update(2,'rohan',90)
# delete(1)
print(view())



