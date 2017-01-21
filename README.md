# Twitter Sentiment Analysis using Python

## PART A

### Twitter API : Streaming API

#### DESCRIPTION AND METHOD

The twitter API uses fetch_sample module in the python script to fetch tweets live. While the python script is ran on Terminal, the output is written into streaming_output_full_pat.txt

**Command used** : -``` python3 fetch_tweets_pat.py -c fetch_samples > streaming_output_full_pat.txt```

To get the first 20 lines of the streaming_output_full_pat.txt file we run : -

**Command used** : - ```head -n 20 streaming_output_full_pat.txt > streaming_output_short_pat.txt```


### Search API

#### DESCRIPTION AND METHOD

In the python script given function fetch_by_term, tweets are searched with respect to a particular term

The term that I used is "Love"

**Command used** : - ```python3 fetch_tweets_pat.py -c fetch_by_terms -term "Love" > search_output_pat.txt```

The search_output_pat.txt contains 100 tweet with the term "Love"
**Term** - "Love"
Example tweets with the term "Love": -

"I haven\'t been told \\"I love you\\" in what seems like foreverrrr \\u2639"
"RT @MakeupsDIY: Love this https:\\/\\/t.co\\/Pq1MVtkXss"
"Love this https:\\/\\/t.co\\/Pq1MVtkXss"
"RT @shorty_hoop: I don\'t love often, but when I do.. I love hard. \\ud83d\\ude29","entities"
"I don\'t love often, but when I do.. I love hard. \\ud83d\\ude29"

### User API

#### DESCRIPTION AND METHOD

In the python script given function fetch_by_user_name, tweets are searched with respect to a given user name. The user names are already given in user_names.txt

**Command used** : - ```python3 fetch_tweets_pat.py -c fetch_by_user_names -file user_names.txt > breaking_bad_tweets_pat.csv```

### Compute term frequency

#### DESCRIPTION AND METHOD

**Command used** : - ```python3 frequency_pat.py <stopword_file> <tweet_file> > term_freq_pat.txt```

In this program we calculate the term frequency of every term that occurs the tweet file  streaming_output_full_pat.txt. First the data is extracted from the file and cleaned. After this the stop words that are mentioned in the file stopwords.txt are removed from the tweets. This is done to remove irrelevant words such as the and and. Then the uniquely occurring words are found and their frequency is calculated and printed. The 30 most 
frequent terms are given below: -

_____30 most frequent terms along with their frequencies_____

rt  0.05569398
i'm  0.00542283
amp  0.00493429
new  0.00478773
get  0.00454346
like  0.00449460
don't  0.00395720
love  0.00371293
one  0.00371293
people  0.00337095
u  0.00293126
time  0.00288241
it's  0.00273584
weather  0.00254043
good  0.00249157
want  0.00239386
can't  0.00229616
think  0.00229616
day  0.00214959
really  0.00210074
go  0.00205188
make  0.00200303
video  0.00195417
would  0.00195417
via  0.00190532
work  0.00190532
need  0.00185647
2  0.00175876
free  0.00175876
going  0.00175876


### CODE SNIPPETS USED

**link** - http://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-python-list

**Code** -
```
def remove_values_from_list(the_list, val):
   
	return [value for value in the_list if value != val]
```   
**Purpose** -  For removing stopwords

**link** - http://stackoverflow.com/questions/15740579/python-how-to-remove-punctuation-in-between-words

**Code** -
```
word.strip(punctuation) for word in line.split()
```
**Purpose** -  Cleaning data

### NOTE

The format of this report file may change in different Operating Systems.

Some of the tweets in the streaming_output_full.txt file with a negative sentiment score have vulgar words and were NOT manipulated and are live tweets from streaming API of TwitterAPI.

### About this project

This project was done as a part of CS 491: Introduction to Data Science at UIC.

## PART B

### Determine the sentiment of each tweet

#### DESCRIPTION AND METHOD

In this section initially the sentiment score for each tweet is calculated based on the sentiment score file AFINN-111.txt. The python script first extracts the text object for the tweets in streaming_output_full_pat.txt. After this the data that has been extracted is cleaned. And then the AFINN-111.txt is parsed and the sentiments  which have one single word are put into a list and sentiments with more than one words are put into a different list. This is the handle bi-words. For example, ‘good’ is handled, ‘good one’ is handled, also sentiment which occur with a dash are also handled such as ‘self-confident’ , in this particular case it can occur as ‘self-confident’ or ‘self confident’ which are also handled. A sentiment upto any number of words can be handled. After this the code checks the tweets with respect to the sentiments and sentiment scores. The scores are summed and printed in descending order.

**Command used**: - ```python3 tweet_sentiment_pat.py <sentiment_file> <tweet_file> > tweet_sentiment_pat.txt```

**top 10 and bottom 10 tweets along with their sentiment score**

13.0  :  RT @TheNikkiDuBose: Thank you everyone for all of your kind words, love and support on my birthday. 31 feels amazing. I feel so... https://â€¦
12.0  :  RT @MyproteinUK: SPRING IS HERE! ðŸ¥ðŸŒ¸ðŸŽ‰ FOLLOW &amp; RT to be in with a chance of winning Â£100 of NEW gym clothing! Ends 10pm, good luck! https://â€¦
11.0  :  Happy Birthday @__maclean hope you have had a good day! Love you lots xxx https://t.co/DiG1aUckJa
11.0  :  RT @mckennafink22: @sammybby_11 happy birthday beautiful hope it's a great oneâ¤ï¸
11.0  :  @Harry_Styles you deserve the most genuine love and happiness. thank you for all you do. mind following me? love you very mucháµ•Ìˆ  -162.105
10.0  :  Happy birthday @johnmeighan444, hope you have an amazing day!! Wouldn't want anyone else dating my bestfriendðŸ¤‘ðŸ˜‡ðŸŽ‰ðŸŽˆðŸŽ
10.0  :  RT @OnlyInBOS: CONTEST! RT+Follow @OnlyInBOS to enter to win a $50 gift card to @TamoBoston! DM winner 10pm. https://t.co/SzJO3Eccta
10.0  :  RT @JJatbest: GIVEAWAY #2!!  rt &amp; follow for a chance to win 6 Polaroid photos of your choice!! winner randomly chosen on 4/1!! https://t.câ€¦
10.0  :  fabulous evening celebrating the life of #peterfranks @TFIGroup. Lovely to see so many industry friends including @rebeccadeniz #eventprofs
10.0  :  Hi @Real_Liam_Payne your smile brightens my days, keep smiling because you deserve to be happy. I love you so much â™¥ Follow me ? â”€11,369
-8.0  :  I didn't wanna do it but you tried me on that fuck shit! ðŸŽ¶
-9.0  :  @TheGSoulhunter fuck u bitch
-9.0  :  I just did the dumbest shit ever and like at the worst time too fuck my life
-9.0  :  salty ass bitch coming for my character
-9.0  :  Damn that was a bomb ass nap! ðŸ‘
-10.0  :  I can't subtweet Wroble because he's a no Twitter havin ass bitch
-10.0  :  Fear of being annoying,  Fear of Typo's , Fear of not being woke enough, Fear in general..."@notyourtypo: Why don't people chat first?"
-11.0  :  I hate bitches that get on here to tweet that they hate Twitter
-12.0  :  RT @RetsOrFavs: Should Oliver &amp; Felicity get married?  RT for HELL YES IT'S ABOUT DAMN TIME ðŸ‘°ðŸ¼â¤ï¸ðŸ‘±ðŸ»  FAV for HELL NO ðŸ˜¡ðŸ‘ŽðŸ»ðŸ˜•  #Olicity https://â€¦
-16.0  :  Filthy Cunt #Nasty #Gangbang Double ##Anal: Tweet The post Filthy Cunt Nasty Gangbang Doubleâ€¦ https://t.co/Wt3K9ophi0


### Happiest Breaking Bad actor

#### DESCRIPTION AND METHOD

In this section the average sentiment score the calculated with breaking_bad_tweets_pat.csv  file which was obtained earlier. First the tweets from the .csv file are extracted and the tweets are cleaned.  And then the AFINN-111.txt is parsed and the sentiments which have one single word are  put into a list and sentiments with more than one words are put into a different list. This is the handle  bi-words. For example, ‘good’ is handled, ‘good one’ is handled, also sentiment which occur with a dash are also handled such as ‘self-confident’ , in this particular case it can occur as ‘self-confident’ or ‘self confident’ which are also handled. A sentiment upto any number of words can be handled. After this the code checks the tweets with respect to the sentiments and sentiment scores. Now, the tweets  and their respective scores are grouped according to the user-name. After grouping the user-name and average sentiment score for each user-name, the average score and user-name are printed in descending order. 

**Command used**: - ```python3 happiest_actor_pat.py <sentiment_file> <csv_file> > happiest_actor_pat.txt```

**the average sentiment score for each actor**

2.130000  :  mrbobodenkirk
2.061224  :  Krystenritter
1.797980  :  quiethandfilms
1.606061  :  CharlesEbaker
1.591398  :  aaronpaul_8
1.587629  :  RjMitte
1.470000  :  deanjnorris
1.450000  :  betsy_brandt
1.260417  :  LuisMoncada77
1.260000  :  BryanCranston
1.104167  :  DanielMoncada80
0.010417  :  mattjonesisdead


### Happiest State

#### DESCRIPTION AND METHOD

In this section the happiest state is determined using the tweets in streaming_output_full_pat.txt  and the sentiment scores given in AFINN-111.txt. Particularly in this section the tweets cannot just be  extract all tweets from the tweet file. The tweets which only have a valid state from the United States can be used. The first object that is considered the tweet[‘place’] object where the tweet[‘place’][‘place_type’] has the values ‘admin’ or ‘city’, the other values are ignored. If this object is equal to these values the state is extracted from tweet[‘place’][‘full_name’] using the predefined in the code all states in USA dictionary  called state_dict. If the particular tweet does not have a tweet[‘place’] object, the tweet[‘user’][‘location’] is considered. The challenge in finding the state name in this object is that it can be re-initialized to anything by the user. Therefore the objects values which do not match state_dict are ignore. In the part of the code  bi-words are taken into consideration such as ‘New Jersey’ and ‘New York’. After the place is being extracted the respective tweet is extracted.  And then the AFINN-111.txt is parsed and the sentiments which have one  single word are put into a list and sentiments with more than one words are put into a different list. This is the  handle bi-words. For example, ‘good’ is handled, ‘good one’ is handled, also sentiment which occur with a dash  are also handled such as ‘self-confident’ , in this particular case it can occur as ‘self-confident’ or ‘self confident’  which are also handled. A sentiment upto any number of words can be handled. After this the code checks the tweets with respect to the sentiments and sentiment scores. Now, the tweets and their respective scores are grouped according to the state. After grouping the state and average sentiment score for each state, the average score and state are printed in descending order. 

**Command used**: - ```python3 happiest_state_pat.py <sentiment_file> <tweet_file> > happiest_state_pat.txt```

**5 happiest states and 5 unhappiest states**

_____5 Happiest States_____

6.000000  :  NH
3.166667  :  OR
2.000000  :  ME
2.000000  :  MN
2.000000  :  CT

_____5 Unhappiest States_____

-0.750000  :  MI
-1.000000  :  AR
-1.500000  :  KS
-1.666667  :  ID
-2.000000  :  RI


### CODE SNIPPETS USED

**link** - http://stackoverflow.com/questions/15740579/python-how-to-remove-punctuation-in-between-words

**Code** -
```
word.strip(punctuation) for word in line.split()
```
**Purpose** -  Cleaning data

### NOTE

The format of this report file may change in different Operating Systems.

Some of the tweets in the streaming_output_full.txt file with a negative sentiment score have vulgar words and were NOT manipulated and are live tweets from streaming API of TwitterAPI.

### About this project

This project was done as a part of CS 491: Introduction to Data Science at UIC.
