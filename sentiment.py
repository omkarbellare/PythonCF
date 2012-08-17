import math
import urllib,urllib2
import os

def compute_sentiment():
    path = 'cars\Reviews'
    listing = os.listdir(path)
    os.chdir(path)

    output_file = open('sentiment_scores.txt','w')
    
    for infile in listing:
        f_in = open(infile,'r')
        file_string = f_in.readlines()
        file_string = file_string[0:50000]
               
        url='http://text-processing.com/demo/sentiment/'
        values = {'text':file_string}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()

        try:
            start = the_page.find('neutral: ')
            end = the_page.find('<',start+1)
            neutral = float(the_page[start+len('neutral: '):end])

            start = the_page.find('polar: ')
            end = the_page.find('<',start+1)
            polar = float(the_page[start + len('polar: '):end])

            start = the_page.find('pos: ')
            end = the_page.find('<',start+1)
            pos = float(the_page[start + len('pos: '):end])

            start = the_page.find('neg: ')
            end = the_page.find('<',start+1)
            neg = float(the_page[start + len('neg: '):end])

        except ValueError:
            continue

        sentiment_score = (0.25*neutral + 0.5*polar*pos)/0.5

        output_file.write(str(sentiment_score)+"\n")

        f_in.close()

    output_file.close()

compute_sentiment()
