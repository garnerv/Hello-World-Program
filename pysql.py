import pymysql
conn = pymysql.connect(unix_socket='/tmp/mysql.sock', user='lrngsql', passwd='secret123', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages")
print(cur.fetchone())
cur.close()
conn.close()