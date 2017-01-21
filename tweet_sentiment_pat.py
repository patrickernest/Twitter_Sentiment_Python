#####################################################################################################
#####################################################################################################

# PART B : Determine the sentiment of each tweet 

#####################################################################################################

import sys
import json
import string
import chardet
def main():
	sent_file = open(sys.argv[1])
	#tweet_file = open(sys.argv[2])
	#TODO: Implement
	sent=[]
	for line in sent_file:
		l=line.strip()
		sent.append(l)
	filename = sys.argv[2]

#####################################################################################################
#
# The tweets from streaming_output_full.txt is extracted and cleaned
#
#####################################################################################################

	with open(filename,'r+') as tweet_file:
		twe = []
		tweet_text=[]
		c=0
		for line in tweet_file:
			tweet=json.loads(line)
			t=tweet['text']
			tweet_text.append([])
			tweet_text[c].append(t)
			ts=[word.strip(string.punctuation) for word in t.split(" ")]
			while '' in ts:
				ts.remove('')
			twe.append([])
			for i in range(0,len(ts)):
				
				encoding = chardet.detect(ts[i].encode("utf-8"))
				if ts[i]!="\n" and encoding['encoding'] == 'ascii':
					ts[i]=ts[i].lower().replace('\n', "").strip()
				twe[c].append(ts[i])
			c=c+1

#####################################################################################################
#
# The sentiment words given in AFINN-111.txt are processed to resolved scores for the sentiment words
# which have a space or a dash such as "good one" and "short-sighted"
#
#####################################################################################################

	senti=[]
	for i in range(0,len(sent)):
		sents=sent[i].split("\t")
		sents[1]=float(sents[1])
		senti.append(sents)
	sent_nospa=[]
	sent_spa=[]
	for i in range(0,len(senti)):
		if (' ' in senti[i][0] or '-' in senti[i][0]):
			sent_spa.append(senti[i])
		if '-' in senti[i][0]:
			sent_nospa.append(senti[i])
		else:
			sent_nospa.append(senti[i])
#####################################################################################################
#
# Checking tweets for sentiments with single word such as "good"
#
#####################################################################################################
	for i in range(0,len(twe)):
		tweet_text[i].append(0)
	for i in range(0,len(twe)):
		for j in range(0,len(twe[i])):
			for k in range(0,len(sent_nospa)):
				if (twe[i][j]==sent_nospa[k][0]):
					tweet_text[i][1]=tweet_text[i][1]+sent_nospa[k][1]
#####################################################################################################
#
# Checking tweets for sentiments which have multiple words and have a dash such as "good one" and
# "short-sighted"
#
#####################################################################################################
	for i in range(0,len(twe)):	
		for k in range(0,len(sent_spa)):
			if ' ' in sent_spa[k][0]:
				sents_spa=sent_spa[k][0].split(' ')
			elif '-' in sent_spa[k][0]:
				sents_spa=sent_spa[k][0].split('-')
			score=multi_sent(sents_spa,sent_spa[k][1],twe[i],sent_nospa)
			if(score):
				tweet_text[i][1]=tweet_text[i][1]+score
#####################################################################################################
#
# Removing new line to print result in single line
#
#####################################################################################################
	
	for i in range(0,len(tweet_text)):
			if '\n' in tweet_text[i][0]:
				tweet_text[i][0]=tweet_text[i][0].replace('\n',' ')
	
	t_text_sort=sorted(tweet_text,key=lambda l:l[1], reverse=True)
	for i in range(0,10):
		print (t_text_sort[i][1]," : ",t_text_sort[i][0])
	for i in range(-10,0):
		print (t_text_sort[i][1]," : ",t_text_sort[i][0])

#####################################################################################################
#
# multi_sent checks sentiments with multiple words and with a dash such as "good one" and "short-sighted"
#
#####################################################################################################

def multi_sent(s_spa,sco,twe,s_no):
	score=0
	twe_len=len(twe)
	for i in range(0,len(twe)-1):
		flag=0
		num=0
		for j in range(0,len(s_spa)):
			if flag==0 and (i+j)<twe_len:
				f2=check(twe[i+j],s_spa[j])
				if num < j:
					num=j
				if(f2==False):
					flag=1
		if flag==0:
			sco1=no_spa_check(twe[i],s_no,twe,num)
			score=score-sco1			
			score=score+sco
	
	return (score)

#####################################################################################################
#
# check compares tweet word and sentiment word for multi_sent
#
#####################################################################################################

def no_spa_check(twe_w,s_no,twe,num):
	score=0
	for j in range(0,len(s_no)):
		n=0
		while n<=num:
			if twe[(twe.index(twe_w))+n]==s_no[j][0]:
				score=score+s_no[j][1]
			n=n+1
	return score

def check(twe_w,s_spa_w):
	if twe_w==s_spa_w:
		return True
	else:
		return False
					
	
if __name__ == '__main__':
	main()
