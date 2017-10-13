import urllib2
import re
response = urllib2.urlopen("http://catalog.registrar.ucla.edu/ucla-catalog2017-348.html")
 
m = re.findall ( '<span class="coursetitle">(.*?)</span>', response.read(), re.DOTALL)

# for x in m:
#     print x, '\n'


csurl = re.findall('<a class="main" href="(.*?)">Computer Science</a></td>', response.read(), re.DOTALL)

print csurl

#m = re.findall ( '<span class="coursetitle">(.*?)</span>', response.read(), re.DOTALL)
