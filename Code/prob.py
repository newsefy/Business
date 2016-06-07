#probability of different values


from __future__ import division
import os
import re

query_dic_final=dict()


def class_dict():
	class_dic=dict()
	class_dic["business"]=510
	class_dic["sport"]=510
	class_dic["politics"]=417
	class_dic["tech"]=401
	class_dic["entertainment"]=385
	return class_dic

def total_no_of_doc(**ka):
	for i in ka:
		total_no_of_doc=total_no_of_doc+int(ka[i])
	return total_no_of_doc


def query_parsed_into_dict():
	query_dic=dict()
	#query in query.txt
	#get "global query.txt"
	fin = open('global query.txt',"r")
	for line in fin:
		line.strip()
		words=line.split()
		for word in words:
			query_dic[word]=query_dic.get(word,0)+1
	print query_dic
	fin.close()
	return query_dic
	# i have a query dict ready





def simple_vector_space_model_bit_reprensentation():
	fout_query=open("query.txt","w")
	class_dic=class_dict()
	for k in class_dic:
		i=1
		while i<=class_dic[k]:
			doc_dic=dict()
			fin_doc=reading_file_from_bag_of_rep(i)
			j=0
			sum=0
			for line in fin_doc:
				line=line.strip()
				#print line
				words=line.split()
				#print words[0]
				if words[0] in query_dic:
					sum=sum+1


			s=str(sum)+" "+k+" "+x+"\n"
			query_dic_final[s]=sum
			for k,v in temp:
				string =k+"\n"
				fout_doc.write(string)
				#fout_query.write(s)
			fin_doc.close()
			i=i+1

	fout_query.close()


simple_vector_space_model_bit_reprensentation()


def calculating_the_no_of_documents_containg_the_word():
	#for k in query_dic:
	print "ho"





def caluclate_idf():
	#idf=log()
	print "hey"




def method_to_reduce_the_weight_of_common_occurance_of_terms_in_global_tables():
	fout_query=open("query.txt","w")
	count=dict()
	for k in class_dic:
		i=1
		while i<=class_dic[k]:
			doc_dic=dict()
			reading_file(i)
			j=0
			sum=0
			for line in fin_doc:
				line=line.strip()
				#print line
				words=line.split()
				#print words[0]
				if words[0] in query_dic:
					count[word]=count.get(word,0)+1
					sum=sum+1
			s=str(sum)+" "+k+" "+x+"\n"
			query_dic_final[s]=sum
			for k,v in temp:
				string =k+"\n"
				fout_doc.write(string)
				#fout_query.write(s)
			fin_doc.close()
			i=i+1
	fout_query.close()



def reading_file_from_bag_of_rep(int):
	a=str(i)
	if len(a)==1:
		#x=raw_input("file to read from")
		x="00"+str(i)+".txt"
	elif len(a)==2:
		x="0"+str(i)+".txt"
	else:
		x=str(i)+".txt"
	s="C:\\Users\\Sagar Gupta\\Desktop\\Business\\Bags_of_words Rep\\"
	rel=s+k
	ab=os.path.join(rel,x)
	fin_doc=open(ab,"r")
	print "opened",x
	return fin_doc


def sorting_the_dict(*a,**ka):
	temp=list()
	temp=[(v, k) for k, v in dic.items()]
	temp.sort()
	temp.reverse()
	temp=[(k, v) for v, k in temp]
	return temp
	