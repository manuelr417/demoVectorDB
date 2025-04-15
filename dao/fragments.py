from config.dbconfig import pg_config
import psycopg2

class FragmentDAO:
    def __init__(self):
        url = "dbname = %s password=%s host=%s port=%s user= %s" % \
              (pg_config['database'],
               pg_config['password'],
               pg_config['host'],
               pg_config['port'],
               pg_config['user']
               )
        self.conn = psycopg2.connect(url)

    def insertFragment(self, did, content, embedding):
        cursor = self.conn.cursor()
        query = "insert into fragments(did, content, embedding) values (%s, %s, %s) returning fid"
        cursor.execute(query, (did, content, embedding,))
        fid = cursor.fetchone()[0]
        self.conn.commit()
        return fid

    def getFragments(self,emb):
        cursor = self.conn.cursor()
        #query = "select did, fid, distance, content from (select did, fid, embedding <-> %s as distance, content from fragments order by distance) as T(did, fid, distance, content) order by fid"
        #query = "select did, fid, embedding <-> %s, content from fragments order by embedding <-> %s"
        query = ("select did, fid, content from fragments order by embedding <-> %s, fid limit 10")
        cursor.execute(query, (emb,))
        result = []
        for row in cursor:
            result.append(row)
        return result