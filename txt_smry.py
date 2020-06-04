# importing libraries 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

# Input text - to summarize 
#text = "Prolonged air leak after a lung volume reduction operation for pulmonary emphysema is a major cause of morbidity and prolonged hospital stay. Staple line reinforcement is recognized as an effective adjunctive technique for decreasing the occurrence of air leaks after pulmonary wedge resection. Numerous materials have been used for staple-line reinforcement. We use expanded polytetrafluoroethylene sleeves that fit over the arms of surgical staplers to facilitate staple-line reinforcement in both thoracoscopic and open lung volume reduction procedures. The expanded polytetrafluoroethylene sleeves do not require rinsing or special handling; they are easy to use and effective in preventing air leaks. We had no prolonged air leaks or infections in any of the cases in which we used the sleeves."

def summary_func(text):
	# Tokenizing the text 
	stopWords = set(stopwords.words("english")) 
	words = word_tokenize(text) 

	# Creating a frequency table to keep the 
	# score of each word 

	freqTable = dict() 
	for word in words: 
		word = word.lower() 
		if word in stopWords: 
			continue
		if word in freqTable: 
			freqTable[word] += 1
		else: 
			freqTable[word] = 1

	# Creating a dictionary to keep the score 
	# of each sentence 
	sentences = sent_tokenize(text) 
	sentenceValue = dict() 

	for sentence in sentences: 
		for word, freq in freqTable.items(): 
			if word in sentence.lower(): 
				if sentence in sentenceValue: 
					sentenceValue[sentence] += freq 
				else: 
					sentenceValue[sentence] = freq 



	sumValues = 0
	for sentence in sentenceValue: 
		sumValues += sentenceValue[sentence] 

	# Average value of a sentence from the original text 

	average = int(sumValues / len(sentenceValue)) 

	# Storing sentences into our summary. 
	summary = '' 
	for sentence in sentences: 
		if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
			summary += " " + sentence 
	return (summary) 