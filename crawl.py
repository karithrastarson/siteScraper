import urllib
from bs4 import BeautifulSoup
import os
import re




def gatherSources(url, folder, includeExternalLinks):

	#open stream
	urlStream = urllib.urlopen(url)

	#extract the html
	html = BeautifulSoup(urlStream.read(), 'html.parser')

	#extract links
	links = list(set(html.find_all('a')))

	#create a folder for this site
	pageName = urlify(html.title.string)

	if not os.path.exists(folder+pageName):
		os.makedirs(folder+pageName)
	
	#Write entire HTML of site to file
	with open(folder+pageName+"\html.html","w") as fout:
		#do your stuff and write it out
		fout.write(html.prettify().encode('ascii', 'ignore'))

	#Write all links to .txt file
	with open(folder+pageName+"\links.txt","w") as fout:
		for link in links:
			fout.write(link.get('href')+"\n")

   

	return


def urlify(s):
#Helper function to make strings url appropriate

	# Remove all non-word characters (everything except numbers and letters)
	s = re.sub(r"[^\w\s]", '', s)

	# Replace all runs of whitespace with a single dash
	s = re.sub(r"\s+", '-', s)

	return s

#Test the function
gatherSources ("http://www.novonordisk.com/", "C:\Users\kari.prastarson\Desktop\\", False)