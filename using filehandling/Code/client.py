#client
#to classify the news article

from __future__ import division
import os
import re


#classification


#taking a text input
#should be present in the same folder as the code
#give the name of the file with the  extension
s=raw_input("give the name of the file with the  extension")

fin=open(s,"r")
#for each word run the logistic regression model to check the best fit
#but before try to build a bag of word reprentation of the text file

for line in fin:
	line.strip()
	#to remove the end \n 
	words=line.split()
	#to get a list of words
	for word in words:
		doc_dict[word]=doc_dict.get(word,0)+1

fin.close()







