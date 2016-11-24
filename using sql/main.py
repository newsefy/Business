import createdb
import query
from bow import BOW
import os
import re
import sys
import logging


def get_doc_map():
	"""
	This function gets the map between the document names and their corresponding table names
	"""
	fil=open("doc_map.txt","r")
	doc_map={}
	for line in fil:
		line=line.strip()
		k=line.split()[0]
		v=line.split()[1]
		#print k+":"+v
		doc_map[k]=v
	fil.close()
	return doc_map

def get_query_setup():
	"""
	This function sets up for querying operations by defining the total number of documents and total number of words
	"""
	fil=open("query_setup.txt","r")
	lst=[]
	for line in fil:
		line=line.strip()
		lst.append(line)
	fil.close()
	return lst	

def set_database():
	"""
	This function sets up the database for the corpus documents
	"""
	corpus="/home/mudit/git_repo/News/Corpus"
	ch=raw_input("1.Set corpus path\n2.Use default path\n")
	if ch==1:
		corpus=raw_input("Enter complete path of corpus:")
	cwd=os.getcwd()
	db=createdb.database()
	doc_list=BOW(db,corpus,cwd)
	N=db.get_no_of_doc()
	Total_words=db.get_total_words()
	print "Number of documents in corpus:"+str(N)
	print "Total number of words:"+str(Total_words)
	fil=open("query_setup.txt","w")
	fil.write(str(N)+"\n")
	fil.write(str(Total_words)+"\n")
	fil.close()
	fil2=open("doc_map.txt","w")
	temp=[(k,v) for k,v in doc_list.items()]
	for k,v in temp:
		fil2.write(str(k)+" "+str(v)+"\n")
	fil2.close()	


if __name__=="__main__":

	 ##Main function that executes the code
	print "-----Querying using Okapi BM-25 Algorithm----"
	ch=raw_input("Initialise database?(Y/N)\n")
	if ch=='Y':
		logging.basicConfig(filename="LOG_IR_A1.log",level=logging.INFO)
		set_database()
		print "---DATABASE SUCCESSFULLY INITIALISED---"
	lst=get_query_setup()
	N=int(lst[0])
	#print "N=%d"%N
	Total_words=int(lst[1])
	#print "total_words=%d"%Total_words
	doc_map=get_doc_map()
	#print doc_map
	ch=raw_input("Start Querying?(Y/N)\n")
	if ch=='Y':
		query=query.Querying(N)
		query.set_AverageDocLength(Total_words)
		while True:
			query.Get_query()
			query.processQuery(doc_map)
			ch=raw_input("Enter another query?(Y/N):")
			if ch=='N':
				break;	
	else:
		exit(0)
