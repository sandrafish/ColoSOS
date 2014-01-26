
import urllib
import zipfile

# the url i want to get

URL = "http://tracer.sos.colorado.gov/PublicSite/Docs/BulkDataDownloads/2014_ContributionData.csv.zip"

#the web connection
web_cnx = urllib.urlopen(URL).read()

# save the file
with open("2014_ContributionData.csv.zip", "w") as output:
     output.write(web_cnx)
output.close()

#unzip the file
zip = zipfile.ZipFile("2014_ContributionData.csv.zip", 'r')
zip.extractall()
zip.close()

# change the encoding
sourceEncoding = "iso-8859-1"
targetEncoding = "utf-8"
source = open("2014_ContributionData.csv")
target = open("2014_ContData.csv", "w") 
target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))

# second URL to get
URL = "http://tracer.sos.colorado.gov/PublicSite/Docs/BulkDataDownloads/2013_ContributionData.csv.zip"

#the web connection
web_cnx = urllib.urlopen(URL).read()

# save the file
with open("2013_ContributionData.csv.zip", "w") as output:
     output.write(web_cnx)
output.close()

#unzip the file
zip = zipfile.ZipFile("2013_ContributionData.csv.zip", 'r')
zip.extractall()
zip.close()

# strips the first line out of the 2013 file and creates a new file
f = open('2013_ContributionData.csv', 'r')
n = open('2013Cont.csv', 'w')
for line in f:
   	if line.startswith('"CO_ID",'):
   		continue
	n.write(line)
f.close()
n.close()

# change the encoding
sourceEncoding = "iso-8859-1"
targetEncoding = "utf-8"
source = open("2013Cont.csv")
target = open("2014_ContData.csv", "a") 
target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))

