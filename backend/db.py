import sqlite3


def create_db():
    con = sqlite3.connect('mydatabase.db')
    # Create Table
    con.execute('''CREATE TABLE IF NOT EXISTS ptt_beauty
             (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
             TITLE           TEXT    NOT NULL,
             URLS        TEXT,
             DATE        TEXT,
             HREF        TEXT);''')
    con.close()


if __name__=='__main__':
    # create_db()
    # SELECT TABLE
    con = sqlite3.connect('mydatabase.db')

    for row in con.execute('''SELECT * from ptt_beauty
                              WHERE ID = 1;
                           '''):
        print(row)
    con.close()
