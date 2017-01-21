#####################################################################################################
#####################################################################################################

# PART B : Happiest State 

#####################################################################################################

import sys
import json
import string
import chardet
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#TODO: Implement
	sent=[]
	for line in sent_file:
		l=line.strip()
		sent.append(l)
	filename = sys.argv[2]
	with open(filename,'r+') as tweet_file:
		twe = []
		tweet_text=[]
		c=0
		twe_state=[]

#####################################################################################################
#
# The states and its abbreviations are being stored in state_dict
#
#####################################################################################################

		state_dict={"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","DC":"District of Columbia","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}

#####################################################################################################
#
# Finding the which state that the tweet belongs to. Here the objects tweet['place'] and tweet['user']
# have been taken into consideration. First the tweet['place'] has been checked and if the tweet has
# the object, the corresponding state and tweet are appended. Then if the tweet does not contain and 
# tweet['place'] object then tweet['user']['location'] is considered. In tweet['user']['location'], there
# need not be a valid location therefore, the object is checked with state_dict for a valid state. Also
# states with a bi-word has been checked and resolved
#
#####################################################################################################

		for line in tweet_file:
			tweet=json.loads(line)
			t=tweet['text']
			if tweet['place']!=None and tweet['place']['country_code']=='US' and tweet['lang']=='en':
				if tweet['place']['place_type']=='admin':
					states=(tweet['place']['full_name']).split(',')
					for key in state_dict:
						if state_dict[key]==states[0]:
							twe_state.append(key)
				if tweet['place']['place_type']=='city':
					states=(tweet['place']['full_name']).split(',')
					for i in range(0,len(states)):
						states[i]=states[i].strip()
					twe_state.append(states[1])
				tweet_text.append([])
				tweet_text[c].append(t)
				ts=[word.strip(string.punctuation) for word in t.split(" ")]
				while '' in ts:
					ts.remove('')
				twe.append([])
				for i in range(0,len(ts)):
					if ts[i]!="\n":
						ts[i]=ts[i].lower().replace('\n', "").strip()
					twe[c].append(ts[i])
				c=c+1
			elif tweet['user']['location']!=None and tweet['lang']=='en':
				flag=0
				loc=tweet['user']['location']
				locs=[word.strip(string.punctuation) for word in loc.split(" ")]
				while '' in locs:
					locs.remove('')
				locs1=[]
				for i in range(0,len(locs)):
					encoding = chardet.detect(locs[i].encode("utf-8"))
					if locs[i]!="\n" and encoding['encoding'] == 'ascii':
						locs[i]=locs[i].replace('\n', "").strip()
						locs1.append(locs[i])
				for loc in locs1[::-1]:
					for key in state_dict:
						if state_dict[key].lower()==loc.lower() or key==loc:
							twe_state.append(key)
							flag=1
					if flag==1:
						break
				if flag!=1:
					for key in state_dict:
						if ' ' in state_dict[key]:
							if (len(locs1)!=0):
								check=check_bi_state(locs1,state_dict[key])
								if check==True:
									flag=1
									twe_state.append(key)								
				if flag==1:
					tweet_text.append([])
					tweet_text[c].append(t)
					ts=[word.strip(string.punctuation) for word in t.split(" ")]
					while '' in ts:
						ts.remove('')
					twe.append([])
					for i in range(0,len(ts)):
						if ts[i]!="\n":
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
# Calculating the sentiments score for each tweet. Then finding the average and grouping
# the states and printing in descending order
#
#####################################################################################################

	state_score=[]	
	for i in range(0,len(twe)):
		score=cal_score(twe[i],sent_spa,sent_nospa)
		state_score.append(score)
	twe_state_u=set(twe_state)
	t_state_uu=list(twe_state_u)
	state_avg={}
	for i in range(0,len(twe)):
		if twe_state[i] in state_avg:
			state_avg[twe_state[i]][0]=state_avg[twe_state[i]][0]+state_score[i]
			state_avg[twe_state[i]][1]=state_avg[twe_state[i]][1]+1
		else:
			state_avg[twe_state[i]]=[state_score[i],1]
	state_final=[]
	for key in state_avg:
		state_final.append([key,(state_avg[key][0]/state_avg[key][1])])
	state_final_sort=sorted(state_final,key=lambda l:l[1], reverse=True)
	print ("")
	print ("_____Average Sentiment Scores for States in the Unites States in Descending Order_____")
	print ("")
	for i in range(0,len(state_final_sort)):
		print ("{0:.6f}".format(state_final_sort[i][1])," : ",state_final_sort[i][0])
	#print ("")
	#print ("_____5 Happiest States_____")
	#print ("")
	for i in range(0,5):
		break
		print ("{0:.6f}".format(state_final_sort[i][1])," : ",state_final_sort[i][0])
	#print ("")
	#print ("_____5 Unhappiest States_____")
	#print ("")
	for i in range(-5,0):
		break
		print ("{0:.6f}".format(state_final_sort[i][1])," : ",state_final_sort[i][0])

#####################################################################################################
#
# Checking for bi-word states such as "New York" and "New Jersey"
#
#####################################################################################################

def check_bi_state(locs1,bi_state):
	bi_state_s=bi_state.split(" ")
	for i in range(0,len(locs1)-1):
		flag=0
		for j in range(0,len(bi_state_s)):
			if flag==0 and (i+j)<len(locs1):
				f2=check_mult(locs1[i+j],bi_state_s[j])
				if(f2==False):
					flag=1
		if flag==0:
			return True
	return False

#####################################################################################################
#
# check compares location word and state word for multi_sent
#
#####################################################################################################

def check_mult(locs1_w,bi_w):
	if locs1_w.lower()==bi_w.lower():
		return True
	else:
		return False

#####################################################################################################
#
# Calculates sentiment score for each tweet
#
#####################################################################################################
		
def cal_score(ts,sent_spa,sent_nospa):
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
