import MySQLdb
from collections import defaultdict
import porter2
import sys
import nltk
import math

class Querying:
    """
    This class defines the various methods required for querying using OKAPI BM-25 Algorothm
    """

    
    def __init__(self,N=0,query='',usID='f2014017',pswd='pass',dbase='IR_assign_14017_14030',hst='localhost'):
        """
        Constructor for Querying object
        """
        self.userID=usID
        self.password=pswd
        self.database = dbase
        self.host = hst
        self.stemming='porter'
        self.n=N
        self.k1=1.5  
        self.b=0.75
        self.query=query
        try:
            self.db = MySQLdb.connect(self.host, self.userID, self.password, self.database)
        except:
            print 'Error initialising database'

    def __del__(self):
        self.db.close()
    
    
    def Get_query(self):
        """
        This Function fetches query from the user
        """
        self.query=raw_input("Enter query:\n")

    def get_TF(self,word,doc_id):
        """
        This function fetches term frequency of a word in a particular document
        """
        cursor=self.db.cursor()
        sql="SELECT TF from %s where TERM='%s'" %(doc_id,word)
        cursor.execute(sql)
        if cursor.rowcount>0:
            temp=cursor.fetchone()[0]
            return temp
        else:
            return 0
        cursor.close()
    
    def calculate_IDF(self,dft):
        """This function calculates the value of idf for a given document frequency(of a given word)"""       
        val=float(self.n)/(dft)
        #print "val="+str(val)
        if val>0:
            return math.log(val)
        else:
            return 0

    def getTermWeight(self,tf,doc_id):
        """
        This function gets the term weight for a term in the query for a given document
        """       
        num=float(self.k1+1)*tf
        #print num
        ld=int(self.get_DocLength(doc_id))
        #print ld
        den=self.k1*((1-self.b)+self.b*float(ld)/self.av_doclen)+tf
        #print den
        return float(num)/den


    def set_AverageDocLength(self,total_words):
        """
        This function sets the Average document length of the database
        """
        self.av_doclen=float(total_words)/(self.n)


    def get_DocLength(self,doc_id):
        """
        This document fetches the document length for a particular doc
        """        
        cursor=self.db.cursor()
        cursor.execute('''SELECT SUM(TF) from %s'''%doc_id)
        if cursor.rowcount > 0:
            return cursor.fetchone()[0]
        else:
            return 0

    def processQuery(self,doc_list):
        """
        This is the main function which calculates scores for all documents and ranks them in decreasing order of score
        """
        #Tokenize query
        #Add punctuation handling functionality
        if '.' in self.query:
            self.query.replace('.',' ')
        if "'" in self.query:
            self.query("'","")
        if "`" in self.query:
            self.query.replace("'","")
        if '''"''' in self.query:
            self.query.replace('''"''',"")
        self.query=self.query.decode("utf8")
        words=nltk.word_tokenize(self.query.lower())
        score={}
        score=defaultdict(lambda:0,score)
        for word in words:

            #Stem words to bring into base form 
            word=porter2.stem(word)
            #print word
            #Fetching Document Frequency of the query word.
            cursor=self.db.cursor()
            sql="SELECT FREQ from DOC_FREQ where WORD='%s'"%word
            cursor.execute(sql)
            if cursor.rowcount>0:
                dft=cursor.fetchone()[0];
                #print dft
                idf=self.calculate_IDF(dft);
            else:
                idf=0
            for doc in doc_list:
                tf=self.get_TF(word,doc)
                #print "tf="+str(tf)
                #print "idf="+str(idf)
                tw=self.getTermWeight(tf,doc)
                #print tw
                score[doc]=score[doc]+idf*tw
                #print "score-%d"%score[doc]
        #We have now calculated the score of documents with respect to our query.
        result=[]
        for doc,score in sorted(score.iteritems(),key=lambda (k,v):(v,k)):
            result.append((doc_list[doc],score))
        result.reverse()
        return self.final_result(result)
    
    def final_result(self,result):
        """
        This function is used to display the final result of the query.This function displays the result of query
        i.e document name and score of that document
        """
        x=raw_input("Enter the number of results you want to view (<="+str(self.n)+"):")
        print("\nThe result in decreasing order of relevance are:-\n")
        for i in xrange(int(x)):
            print(result[i])
