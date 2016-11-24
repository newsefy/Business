import MySQLdb
import sys
import os

class database:
    def __init__(self,usID='sagar', pswd='toor@123', dbase='IR_assign', hst='localhost'):
        self.userID = usID
        self.password = pswd
        self.database = dbase
        self.host = hst
        self.N = 0
        try:
            self.db = MySQLdb.connect(self.host, self.userID, self.password, self.database)
            print "Able to connect to database"
        except:
            print 'Error initialising database'

    def __del__(self):
        self.db.close()

    def create_table_docf(self):    
        #prepare the cursor
        cursor=self.db.cursor()
        #cursor.execute("SELECT VERSION()")
        #data=cursor.fetchone()
        sql='''CREATE TABLE  DOC_FREQ(
                WORD VARCHAR(50),
                FREQ INT,
                PRIMARY KEY(WORD) 
                )'''
        try:
            cursor.execute(sql)
            print "Created table DOC_FREQ"
        except:
            print "Could not create table DOC_FREQ. Table may already be existing"
        finally:
            cursor.close()

    def add_to_doc_freq(self,word,count):
        cursor=self.db.cursor();
        sql="INSERT into DOC_FREQ values ('"+word+"',"+str(count)+")"
        #print sql
        try:
			cursor.execute(sql)
			print "Added word into DOC_FREQ"    
			self.db.commit()
        except:
            print "Error adding word:"+word+" frequency:"+str(count)+" into DOC_FREQ"
        finally:
            cursor.close()

    def create_table_doc(self,docname):
        cursor=self.db.cursor()
        sql='''CREATE TABLE %s(TERM VARCHAR(50),TF INT,PRIMARY KEY(TERM))''' %docname
        try:
			cursor.execute(sql)
			print "Created table %s"%docname
        except:
            print "Error creating table for document %s" %docname
            self.db.rollback()
        finally:
            cursor.close()
    
    def insert_into_doc(self,docname,word,count):
		cursor=self.db.cursor();
		sql="INSERT into " + docname +" values ('"+word+"',"+str(count)+")"
        #print sql
		try:
			cursor.execute(sql)
			print "Added word into %s"%docname
			self.db.commit()
		except:
			print "Error inserting word:"+word+" count:"+str(count)+" into table "+docname
			self.db.rollback()
		finally:
			cursor.close()   

    def set_no_of_doc(self,N):
    	self.N=N
    
    def get_no_of_doc(self):
    	return self.N 
    def set_total_words(self,N):
    	self.total_words=N
    def get_total_words(self):
    	return self.total_words  
