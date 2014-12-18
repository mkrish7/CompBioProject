import os
text_path = '/home/satishkumaar/Documents/CSE549/project/test/text/articles_text'
seq = {}
text_files = []
for root, dirs, files in os.walk(text_path):
    for text_file in files:    
        text_files.append(os.path.join(root, text_file))

for text_file in text_files:
    year = text_file.split('/')[-1][:4]
    if year in seq:
        seq[year] += 1
    else:
        seq[year] = 1

print len(seq)
for key in sorted(seq):
    print key + ':' + str(seq[key])
