#####################################################################################################
#####################################################################################################

# PART A : Twitter API : Compute term frequency

#####################################################################################################

import sys
import json
import string
import chardet
def main():
	#TODO: Implement
	stopword_file = open(sys.argv[1])
	filename = sys.argv[2]

#####################################################################################################
#
# First the data from streaming_output_full.txt is parsed and the text object from the tweet is extracted
# and the extracted tweet is cleaned.
#
#####################################################################################################

	with open(filename,'r+') as tweet_file:
		twe = []
		for line in tweet_file:
			tweet=json.loads(line)
			t=tweet['text']
			ts=[word.strip(string.punctuation) for word in t.split(" ")]
			while '' in ts:
				ts.remove('')
			
			for i in range(0,len(ts)):
				encoding = chardet.detect(ts[i].encode("utf-8"))
				if ts[i]!="\n" and encoding['encoding'] == 'ascii':
					ts[i]=ts[i].lower().replace('\n', "").strip()
					twe.append(ts[i])
	stop=[]

#####################################################################################################
#
# Stop are removed from the extracted tweets
#
#####################################################################################################

	for line in stopword_file:
		l=line.strip()
		stop.append(l)
	for i in range(0,len(stop)):
		if stop[i] in twe:
			twe = remove_values_from_list(twe, stop[i])
	occ=len(twe)
	t_u=set(twe)
	term_u=list(t_u)
	twe.sort()
	term_u.sort()
	term_f = []
	term_ffinal = []

#####################################################################################################
#
# Frequency for every occuring term is calculated
#
#####################################################################################################

	for i in range(0,len(term_u)):
		c=0
		for j in range(0,len(twe)):
			if term_u[i] == twe[j]:
				c=c+1
		term_f.append(c)
		term_ffinal.append(c/occ)
	t_final = []
	for i in range(0,len(term_u)):
		t_final.append([])
		print (term_u[i]+"  "+"{0:.8f}".format(term_ffinal[i]))
		t_final[i].append(term_u[i])
		t_final[i].append(term_ffinal[i])
	term_f_copy=sorted(t_final,key=lambda l:l[1], reverse=True)
	#print ("")	
	#print ("_____30 most frequent terms along with their frequencies_____")
	#print ("")
	for i in range(0,30):
		break
		print (term_f_copy[i][0]+"  "+"{0:.8f}".format(term_f_copy[i][1]))

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

if __name__ == '__main__':
    main()

