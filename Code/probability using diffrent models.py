#probability of different values


from __future__ import division
import os
import re
class_dic=dict()
class_dic[business]=510
class_dic[sport]=511
class_dic[politics]=417
class_dic[tech]=401
class_dic[entertainment]=385

#query in query.txt
#get "global query.txt"
fin = open("global query.txt","r")
for lines in fin:
	line=line.strip()
	words=line.split()
	for word in words:
		query_dic[word]=query_dic.get(word,0)+1
fin.close()

# i have a query dict ready

def simple_vector_space_model_bit_reprensentation():

	for k in class_dic:
		while i<class_dic[k]:
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
			i=0
			for line in fin_doc:
				if i<2:
					continue
				else:
					line=line.strip()
					words=line.strip()
					if words[0] in query_dic:
						sum=sum+1
			
			fout.write(s)






			










def second_model():