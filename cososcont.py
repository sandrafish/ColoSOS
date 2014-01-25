<<<<<<< HEAD

=======
>>>>>>> b519ceb463269b595127ff80417f8f2cd9a9686d
import urllib
import zipfile

# the url i want to get
<<<<<<< HEAD
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

=======
>>>>>>> b519ceb463269b595127ff80417f8f2cd9a9686d
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

# change the encoding
sourceEncoding = "iso-8859-1"
targetEncoding = "utf-8"
source = open("2013_ContributionData.csv")
target = open("2013_ContData.csv", "w") 
<<<<<<< HEAD
target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))
=======
target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))
>>>>>>> b519ceb463269b595127ff80417f8f2cd9a9686d
