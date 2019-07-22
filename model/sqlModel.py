from urllib.parse import urlparse
import mysql.connector as mydb


url = urlparse('mysql://user:password@127.0.0.1:3314/account_db?charset=utf8mb4')

conn = mydb.connect(
    host = url.hostname or '127.0.0.1', 
    port= url.port or 3306,
    user = url.username or 'root',
    password = url.password or 'password',
    database = url.path[1:]
)

# print(conn.is_connected())
# conn.ping(reconnect=True)
cur = conn.cursor()

#   追加，アップデート CU
try:
    cur.execute('INSERT INTO accounts (userid, password) VALUES (%s, %s)', ['hoge','hoge'])
    conn.commit()
except:
    conn.rollback()
    raise

# 削除 D
try:
    cur.execute('DELETE FROM accounts')
    conn.commit()
except:
    conn.rollback()
    raise

# 選択 R
cur.execute('SELECT * FROM accounts')
print(cur.fetchall())
conn.commit()

cur.close()
conn.close()