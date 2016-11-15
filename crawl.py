import urllib
import lxml.html

url = "http://www.novonordisk.com/"
t = lxml.html.parse(url)
print t.find(".//title").text
