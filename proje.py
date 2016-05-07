import webbrowser as wb
import urllib

def indir (keywords):

	url = 'https://kat.cr/usearch/'
	keywords = keywords.split(' ')
	liste = '%20'.join(keywords)
	
	wb.open(url+liste+'/')


keywords = raw_input('film adini giriniz:\t')
indir(keywords)
