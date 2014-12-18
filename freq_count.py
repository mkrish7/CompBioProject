import glob
import os
import operator

word_freq = {}

stop_words = set()

with open('stopwords.txt', 'r') as sf:
    for line in sf:
        stop_words.add(line.strip())

documents = []
def listDocuments():
	os.chdir("1710")
	for document in glob.glob("*.txt"):
		# print('Reading '+document)
		documents.append(document)

listDocuments()

for file_name in documents:
    with open(file_name) as in_file:
        lines = in_file.readlines()
        for line in lines:
            words = line.lower().split()
            for word in words:
                if word in stop_words or not word.isalpha():
                    continue
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1                
os.chdir("../")
out_file = open('result.txt','w')

sorted_dic = sorted(word_freq.items(), key=operator.itemgetter(1))

out_file.write(str(sorted_dic[-50:]))
