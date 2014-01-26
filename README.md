ColoSOS
=======

Colorado Secretary of State bulk download files

These two files allow you to download, unzip and change encoding for bulk downloads from the Colorado Secretary of State's <a href="http://tracer.sos.colorado.gov/PublicSite/DataDownload.aspx">bulk download area.</a>

If you are using a PC, you may not need the encoding section. It is necessary for Mac OS X, however.

These files have been updated to include the new 2014 files, and merge them into a single file.

These files typically need some cleanup before importing into a database; i typically use csv kit: csvclean -n 2014_ContData.csv , for instance.
