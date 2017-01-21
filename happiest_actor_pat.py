#####################################################################################################
#####################################################################################################

# PART B : Happiest Breaking Bad actor 

#####################################################################################################

import sys
import csv
import string
import chardet
def main():
	sent_file = open(sys.argv[1])
	csv_file = open(sys.argv[2])
	file_reader = csv.reader(csv_file)
	#TODO: Implement
#####################################################################################################
#
# The sentiment words given in AFINN-111.txt are processed to resolved scores for the sentiment words
# which have a space or a dash such as "good one" and "short-sighted"
#
#####################################################################################################
	sent=[]
	for line in sent_file:
		l=line.strip()
		sent.append(l)
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
	bb_t=[]
	bb_user=[]
	c=0
	for row in file_reader:
		bb_user.append(row[0])
		bb_t.append([])
		for i in range(0,len(row)):
			bb_t[c].append(row[i])
		c=c+1
	bb_user2=[]
	for i in range(1,len(bb_user)):
		bb_user2.append(bb_user[i])
	bb_uuni=set(bb_user2)
	bb_uu=list(bb_uuni)
	bb_uu.sort()
	bb_score=[]

#####################################################################################################
#
# Calculating the sentiments score for each user for each tweet. Then finding the average and grouping
# the users and printing in descending order
#
#####################################################################################################

	for i in range(0,len(bb_t)):
		score=cal_score(bb_t[i][1],sent_spa,sent_nospa)
		bb_score.append(score)
	bb_avg={}
	for i in range(1,len(bb_user)):
		if bb_user[i] in bb_avg:
			bb_avg[bb_user[i]][0]=bb_avg[bb_user[i]][0]+bb_score[i]
			bb_avg[bb_user[i]][1]=bb_avg[bb_user[i]][1]+1
		else:
			bb_avg[bb_user[i]]=[bb_score[i],1]
	bb_final=[]
	for key in bb_avg:
		bb_final.append([key,(bb_avg[key][0]/bb_avg[key][1])])
	bb_final_sort=sorted(bb_final,key=lambda l:l[1], reverse=True)
	for i in range(0,len(bb_final_sort)):
		print ("{0:.6f}".format(bb_final_sort[i][1])," : ",bb_final_sort[i][0])

#####################################################################################################
#
# The tweets from breaking_bad_tweets.csv is extracted and cleaned and calculates score for each tweet
#
#####################################################################################################
		
def cal_score(tw,sent_spa,sent_nospa):
	ts=[word.strip(string.punctuation) for word in tw.split(" ")]
	while '' in ts:			
		ts.remove('')
	for i in range(0,len(ts)):
		encoding = chardet.detect(ts[i].encode("utf-8"))
		if ts[i]!="\n" and encoding['encoding'] == 'ascii':
			ts[i]=ts[i].lower().replace('\n', "").strip()
	score=0
	for i in range(0,len(ts)):
		for j in range(0,len(sent_nospa)):
				if (ts[i]==sent_nospa[j][0]):
					score=score+sent_nospa[j][1]

	for j in range(0,len(sent_spa)):
		if ' ' in sent_spa[j][0]:
			sents_spa=sent_spa[j][0].split(' ')
		elif '-' in sent_spa[j][0]:
			sents_spa=sent_spa[j][0].split('-')
		score1=multi_sent(sents_spa,sent_spa[j][1],ts,sent_nospa)
		if(score1):
			score=score+score1
	return score

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
