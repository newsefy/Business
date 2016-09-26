import MYSQLdb
import sys

class Indexing:
	def __init__(self, stpwrdfile, usID='sagar', pswd='toor@123', dbase='IR_assign', hst='localhost'):
        self.userID = usID
        self.password = pswd
        self.database = dbase
        self.host = hst
        self.cwd = os.getcwd()
        self.stopWordFile = stpwrdfile
        self.N = 0
        self.query_insert = ''
        try:
            self.db = MySQLdb.connect(self.host, self.userID, self.password, self.database)
        except:
            print 'error initialising database'

    def __del__(self):
        self.db.close()
    def idf_calculation(self,query,):

