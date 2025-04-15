from config.dbconfig import pg_config
import psycopg2

class DocDAO:
    def __init__(self):
        url = "dbname = %s password=%s host=%s port=%s user= %s" % \
              (pg_config['database'],
               pg_config['password'],
               pg_config['host'],
               pg_config['port'],
               pg_config['user']
               )
        self.conn = psycopg2.connect(url)

    def insertDoc(self, docname):
        cursor = self.conn.cursor()
        query = "insert into docs(docname) values (%s) returning did"
        cursor.execute(query, (docname,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid