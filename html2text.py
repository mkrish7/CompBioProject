from bs4 import BeautifulSoup
import glob
import sys
path = '/home/satishkumaar/Documents/CSE549/project/test/articles_html/' + sys.argv[1] + '/'

file_list = glob.glob(path + '*.html')

for f in file_list:
    with open(f, 'r') as html:
        soup = BeautifulSoup(html)
        to_write = soup.get_text()
        with open(f.replace('.html', '.txt').replace('test/articles_html', 'test/articles_text'), 'w+') as w:
            w.write(to_write.encode('utf-8'))
            
