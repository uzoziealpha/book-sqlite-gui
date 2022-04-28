import sqlite3


#create a connection to the DB
def connect():
    conn=sqlite3.connect("books.db")
    #define cursor object
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    #reconnecting to DB
    conn=sqlite3.connect("books.db")
    #define cursor object
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()



def view():
    #reconnecting to DB
    conn=sqlite3.connect("books.db")
    #define cursor object
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
   #conn.commit()
    rows=cur.fetchall()
    conn.close()
    return rows


def search(title="",author="",year="",isbn=""):
    #reconnecting to DB
    conn=sqlite3.connect("books.db")
    #define cursor object
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
     #reconnecting to DB
    conn=sqlite3.connect("books.db")
    #define cursor object
    cur=conn.cursor()
    #delete from book where id is something(?)
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
     #reconnecting to DB
    conn=sqlite3.connect("books.db")
    #define cursor object
    cur=conn.cursor()
    #delete from book where id is something(?)
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()
    


connect()
#insert("The Earth", "Obinna Uzozie", 1911,902323132)
#delete(1)
#update(2,"The hidden colors", "Smooth Rick", 2021, 19937832)
print(search(author="Obinna Uzozie"))
print(view())