import sqlite3

def del_record(data):
    conn = sqlite3.connect('./db/id_record.db')
    
    with conn:
        cur = conn.cursor()
        sql = "delete from id_record where id = {{email}} values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.executemany(sql, data)
        
        conn.commit()