#How many characters are in the 10th, 20th, 30th and 100th lines of HTML from this page:

#http://biostat.jhsph.edu/~jleek/contact.html

library(httr, help, pos = 2, lib.loc = NULL)

con = url("http://biostat.jhsph.edu/~jleek/contact.html")
html <- readLines(con)
close(con)

nchar(html[10])
nchar(html[20])
nchar(html[30])
nchar(html[100])