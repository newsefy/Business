import re
import os
class_dic=dict()
i=1
y=raw_input("file to write to")
fout =open(y,"w")
while i<511:
	doc_dic=dict()
	a=str(i)
	if len(a)==1:
	#x=raw_input("file to read from")
		x="00"+str(i)+".txt"
	elif len(a)==2:
		x="0"+str(i)+".txt"
	else:
		x=str(i)+".txt"

	rel="C:\\Users\\Sagar Gupta\\Desktop\\Business\\Training set\\business"
	rel_ans="C:\\Users\\Sagar Gupta\\Desktop\\Business\\Bags_of_words Rep\\business"
	ab=os.path.join(rel,x)
	ab_doc=os.path.join(rel_ans,x)
	fin=open(ab,"r")
	fout_doc=open(ab_doc,"w")
	print "opened",x
	
	for line in fin:
		line=line.strip()
		words=line.split()
		for word in words:
			#count(word)=count.get(word,0)+1
			doc_dic[word]=doc_dic.get(word,0)+1
			class_dic[word]=class_dic.get(word,0)+1

	#print count
		temp=dict()
		temp=[(v, k) for k, v in doc_dic.items()]
		temp.sort()
		temp.reverse()
		temp=[(k, v) for v, k in temp]

		for k,v in temp:
			string =k+" "+str(v)+"\n"
			fout_doc.write(string)
		#fout.write(v)


	fin.close()
	fout_doc.close()
	i=i+1


voc=len(class_dic)
s=0
for k,v in class_dic.items():
	s=s+v
	#print s

string="vocab size : "+str(voc)+"\n"
fout.write(string)
string = "total global freq : "+str(s)+"\n" 
fout.write(string)
temp=dict()
temp=[(v, k) for k, v in class_dic.items()]
temp.sort()
temp.reverse()
temp=[(k, v) for v, k in temp]


for k,v in temp:
	#prob =format(float(v/s),".50f")
	string =k+" "+str(v)+" "+"\n"
	fout.write(string)
fout.close()