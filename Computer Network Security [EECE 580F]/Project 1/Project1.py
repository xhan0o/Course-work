import operator

file=open("text.txt","r+")  #opening input file name 'text.txt'
totalwords=0
word_dict={}                #dictionary for words

#for counting words, splitting by spacings and stripping special chars. - and ' handled by making combined word.
for line in file.readlines():   #reading line by line
    words=line.lower().split()  #lower case and split by spacing
    for word in words:
        sword=''.join(z for z in word if z.isalnum())   #join all alpha numeric values in word together
        if sword in word_dict:  #same word,+1 to that occurance
            word_dict[sword]['occ'] +=  1
        else:                   #new word add that word to dictionary and make occurance 1
            word_dict[sword] = {'occ' : 1}

    totalwords = totalwords + len(words) #count number of words
print "Total number of words: " , totalwords  #printing total number of words
sorted_worddict = sorted(word_dict.iteritems(), key=operator.itemgetter(1), reverse=True)   #sorting word dictionary for csv export
#pprint (sorted_worddict) debug

for key, value in sorted_worddict: #getting Frequency of words
    value['freq'] = float(value['occ'])/float(totalwords)
#pprint (sorted_worddict) debug

file.seek(0)    #File pointer reset at 0
s=file.read()
sentencecount=s.count('. ') + s.count('! ') + s.count('? ') + s.count('" ') #counting sentences sentences ending with .,!,?," + must have space after that
thecount = s.lower().count('. the ') + s.lower().count('? the ') + s.lower().count('! the ') + s.lower().count(' "the ') #counting sentences starts with 'the' by same logic of above
print "Total number of sentences:", sentencecount     #printing total number of sentences
print ("Occurance of 'the' at start of sentence and Frequency: " +
            str(thecount) + " , " + str(float(thecount)/float(sentencecount)))    #printing Occurance and Frequency of 'the' sentences

#most Frequent bigrams with similar logic used for single words
file.seek(0)
twoword=list(file.read().split())   #reading file
i=0
j=1
twoword_dict={}
while (j<len(twoword)):     #true till end of file
    word=twoword[i]+" "+twoword[j]  #making combination of bigrams
    if word in twoword_dict:
        twoword_dict[word]+=1
    else:
        twoword_dict[word]=1
    i+=1    #counter increment
    j+=1

sorted_twoworddict = sorted(twoword_dict.iteritems(), key=operator.itemgetter(1), reverse=True)     #sorting bigram dictionary
print ("Most Frequent 2 word Combination: " + "('Word', Occurance)  " + str(sorted_twoworddict[0])) #printing most Frequent bigram

#Writing CSV by writting comma saperated values for keys. not using csv funtion
file=open("result.csv","w")    #file name and write permission
for key,value in sorted_worddict:           #loop to write comma saperated values
    file.write(key +"," + str(value['occ'])+","+str(value['freq'])+"\n")    #key,value1,value2 \n
file.close() #closing file
#end of program
