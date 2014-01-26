
import urllib
import zipfile

# the url i want to get
URL = "http://tracer.sos.colorado.gov/PublicSite/Docs/BulkDataDownloads/2013_ExpenditureData.csv.zip"

#the web connection
web_cnx = urllib.urlopen(URL).read()

# save the file
with open("2013_ExpenditureData.csv.zip", "w") as output:
     output.write(web_cnx)
output.close()

#unzip the file
zip = zipfile.ZipFile("2013_ExpenditureData.csv.zip", 'r')
zip.extractall()
zip.close()

# the second url i want to get
URL = "http://tracer.sos.colorado.gov/PublicSite/Docs/BulkDataDownloads/2014_ExpenditureData.csv.zip"

#the web connection
web_cnx = urllib.urlopen(URL).read()

# save the file
with open("2014_ExpenditureData.csv.zip", "w") as output:
     output.write(web_cnx)
output.close()

#unzip the file
zip = zipfile.ZipFile("2014_ExpenditureData.csv.zip", 'r')
zip.extractall()
zip.close()


#f = open(fname).readlines()
#firstLine = f.pop(0) #removes the first line
#for line in f:


# change the encoding and append
sourceEncoding = "iso-8859-1"
targetEncoding = "utf-8"
source = open("2014_ExpenditureData.csv")
target = open("2014_ExpData.csv", "w") 
target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))

# strips the first line out of the 2013 file and creates a new file
f = open('2013_ExpenditureData.csv', 'r')
n = open('2013Exp.csv', 'w')
for line in f:
   	if line.startswith('"CO_ID",'):
   		continue
	n.write(line)
f.close()
n.close()

# change the encoding and append the second file
sourceEncoding = "iso-8859-1"
targetEncoding = "utf-8"
source = open("2013Exp.csv")
target = open("2014_ExpData.csv", "a") 
target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))


