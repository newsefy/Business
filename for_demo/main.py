import createdb
import query
from bow import BOW
import os
import re
import sys

#corpus=raw_input("Enter the directory of corpus (full path):");

corpus="/home/stark/git/Different-news-articles-classified/for_demo/Corpus"
cwd=os.getcwd()
db=createdb.database()
doc_list=BOW(db,corpus,cwd)
N=db.get_no_of_doc()
Total_words=db.get_total_words()
print "Number of documents in corpus:"+str(N)
#print doc_list
query=query.Querying(N)
query.set_AverageDocLength(Total_words)
while True:
	query.Get_query()
	query.processQuery(doc_list)
	ch=raw_input("Enter another query?(Y/N):")
	if ch=='N':
		break;
