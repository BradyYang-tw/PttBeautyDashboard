import sqlite3


def create_db():
    con = sqlite3.connect('mydatabase.db')
    # Create Table
    con.execute('''CREATE TABLE IF NOT EXISTS ptt_beauty
             (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
             TITLE           TEXT    NOT NULL,
             URLS        TEXT UNIQUE,
             DATE        TEXT,
             HREF        TEXT UNIQUE);''')
    con.close()


if __name__=='__main__':
    create_db()
    #SELECT TABLE
    # con = sqlite3.connect('mydatabase.db')
    #
    # for row in con.execute('''SELECT * from ptt_beauty
    #                           WHERE title="[正妹] 1993年";
    #                        '''):
    #     print(row)
    # con.close()
