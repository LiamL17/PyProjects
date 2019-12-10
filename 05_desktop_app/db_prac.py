import sqlite3

def main():

    def create_table():
        conn = sqlite3.connect("../data/lite.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
        conn.commit()
        conn.close()
    
    def insert(item, quan, price):
        conn = sqlite3.connect("../data/lite.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quan, price))
        conn.commit()
        conn.close()

    insert('Water Glass', 100, 0.5)

    def view():
        conn = sqlite3.connect("../data/lite.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM store")
        rows = cur.fetchall()
        conn.close()
        return rows
    
    print(view())

if __name__ == "__main__":
    main()