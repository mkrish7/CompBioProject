import nltk
from nltk.collocations import *
import glob
import os
from sets import Set
from collections import Counter

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

global directory
directory = "/home/mujay/nltk_data/corpora/genesis"
os.chdir(directory)

global documents
documents = []

monogram_file = open('/home/mujay/Desktop/ComputationalBiology/BioMed/dtm_release/dtm/final_run/colocation/monograms.txt', 'w')
bigram_file = open('/home/mujay/Desktop/ComputationalBiology/BioMed/dtm_release/dtm/final_run/colocation/bigrams.txt', 'w')
trigram_file = open('/home/mujay/Desktop/ComputationalBiology/BioMed/dtm_release/dtm/final_run/colocation/trigrams.txt', 'w')

stopword_file = open('/home/mujay/Desktop/ComputationalBiology/BioMed/dtm_release/dtm/final_run/colocation/stopwords.txt', 'r')

stopword_contents = stopword_file.read()
stop_words = stopword_contents.lower().split()

for document in glob.glob("*.txt"):
	fullfile = directory+'/'+document
	if os.path.getsize(fullfile) > 0:
		documents.append(document)

def extractBiGramsAndTriGrams() :
	global words
	words = Set([])

	print "Extracting monograms, bigrams and trigrams from the corpus. Please wait..."

	ignored_words = nltk.corpus.stopwords.words('english')

	iteration = 0
	total = len(documents)	

	ten_percent = total / 10
	next_percent = ten_percent

	print "Total files to be processed : "+str(total)

	for document in documents:
		
		if iteration == next_percent:
			print "Finished processing "+str(next_percent)+" files of "+str(total)+" files.\n"
			next_percent = next_percent + ten_percent

		# Extract Monograms		
		contents = open(document,'r').read()
		in_words = contents.lower().split()

		unique_words = []

		for in_word in in_words:
			if in_word not in stop_words:
				unique_words.append(in_word)
			
		counts = Counter(unique_words).most_common(20)

		monogram_file.write(document+":\n"+str(counts)+"\n\n")

		# Extract Bi and Trigrams
		words = nltk.corpus.genesis.words(document)

		finder_bigrams = BigramCollocationFinder.from_words(words)
		finder_trigrams = TrigramCollocationFinder.from_words(words)

		finder_bigrams.apply_freq_filter(3)
		finder_bigrams.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
	
		finder_trigrams.apply_freq_filter(3)
		finder_trigrams.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
	
		bigram_file.write(document+":\n"+str(finder_bigrams.nbest(bigram_measures.pmi, 20))+"\n\n")
		trigram_file.write(document+":\n"+str(finder_trigrams.nbest(trigram_measures.pmi, 20))+"\n\n")
		
		iteration = iteration + 1
#End of method

extractBiGramsAndTriGrams()

# Close file after writing
monogram_file.close()
bigram_file.close()
trigram_file.close()

