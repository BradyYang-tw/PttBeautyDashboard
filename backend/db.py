import sqlite3


def create_db():
    con = sqlite3.connect('mydatabase.db')
    # Create Table
    con.execute('''CREATE TABLE ptt_beauty
             (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
             TITLE           TEXT    NOT NULL,
             URLS        TEXT,
             DATE        TEXT);''')
    con.close()


if __name__=='__main__':
    # create_db()
    # SELECT TABLE
    con = sqlite3.connect('mydatabase.db')
    for row in con.execute('''SELECT * from ptt_beauty'''):
        print(row)
    con.close()
