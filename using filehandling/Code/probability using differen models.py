#probability of different values


from __future__ import division
import os
import re
class_dic=dict()
class_dic["business"]=510
class_dic["sport"]=510
class_dic["politics"]=417
class_dic["tech"]=401
class_dic["entertainment"]=385
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
# i have a query dict ready
query_dic_final=dict()
def simple_vector_space_model_bit_reprensentation():
	fout_query=open("query.txt","w")

	for k in class_dic:
		i=1
		while i<=class_dic[k]:
			doc_dic=dict()
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
			j=0
			sum=0
			for line in fin_doc:
				#print j
				j=j+1
				if j<=2:
					continue
				else:
					line=line.strip()
					#print line
					words=line.split()
					#print words[0]
					if words[0] in query_dic:
						sum=sum+1


			s=str(sum)+" "+k+" "+x+"\n"
			query_dic_final[s]=sum
			print s
			temp=dict()
			temp=[(v, k) for k, v in doc_dic.items()]
			temp.sort()
			temp.reverse()
			temp=[(k, v) for v, k in temp]
			for k,v in temp:
				string =k+"\n"
				fout_doc.write(string)
				#fout_query.write(s)
			
			fin_doc.close()
			i=i+1

	fout_query.close()


simple_vector_space_model_bit_reprensentation()
