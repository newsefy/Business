import nltk
import os 
import string
import createdb
import porter2


def BOW(db,corpus,cwd):
	"""
	This function creates the bag-of-words representation for all the corpus documents and creates a database for all words.

	"""
	TOTAL_WORDS=0
	doc_freq=dict()
	DOC_LIST=dict()
	doc_dic=dict()
	no_of_doc=0
	words=[]
	#Create the DOCF table
	db.create_table_docf();
	# Execute shell script which get document list from corpus folder
	command="sh getdoclist.sh "+corpus+" "+cwd
	ret=os.system(command)
	if ret!=0:
		print "Error creating document list\n."
		exit(1)		
	stop=string.punctuation #punctuation removed
	#Open file containing name of documents in corpus
	fin=open("doclist","r")
	#Open each document at a time and construct Bag of Words for each document
	
	for line in fin:
		openfile=corpus+"/"+line.strip()
		fdoc=open(openfile,"r")
		no_of_doc+=1
		#Read opened doc line by line
		for sentence in fdoc:
			#convert into lower case and tokenize using nltk
			#Add functionality to handle punctuation '.' and ''
			if '.' in sentence:
				sentence.replace('.',' ')
			if "'" in sentence:
				sentence.replace("'","")
			if "`" in sentence:
				sentence.replace("'","")
			if '''"''' in sentence:
				sentence.replace('''"''',"")
			sentence=sentence.decode("utf8")
			sentence=nltk.word_tokenize(sentence.lower())
			#if wrd from sentence list , not in stop 'list' then add it to a list of words for doc
			for word in sentence:
				if word not in stop:
					#Add suitable stemmer here-Porter
					word=porter2.stem(word)
					doc_dic[word]=doc_dic.get(word,0)+1
					TOTAL_WORDS=TOTAL_WORDS+1
			#for x in words:
			#	print x
		#Create table corresponding to the Doc. Splitting 'doc_name.txt' and creating a table named docname
		docname="d"+line.split('.')[0]
		DOC_LIST[docname]=line.strip();
		db.create_table_doc(docname)
		#All words of the doc are added to words. Now add them to doc db
		#Also updates Doc Freq for the words
		temp=[(word,count) for word,count in doc_dic.items()]
		for word,count in temp:
			doc_freq[word]=doc_freq.get(word,0)+1
			db.insert_into_doc(docname,word,count)
		doc_dic.clear()

	#Close file doc_list
	fin.close()
	#All Documents are processed and their corresponding tables made.
	#Also doc_freq now contains the list of words and the number of documents in which they occur.
	#Set no. of corpus documents
	db.set_no_of_doc(no_of_doc)
	db.set_total_words(TOTAL_WORDS)
	#Add doc_freq to doc_freq table
	temp=[(word,doc_count) for word,doc_count in doc_freq.items()]
	for word,doc_count in temp:
		db.add_to_doc_freq(word,doc_count)
	return DOC_LIST 
