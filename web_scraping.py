import urllib.request
import re
def find_offsets(haystack, needle):
    """
    Find the start of all (possibly-overlapping) instances of needle in haystack
    """
    offs = -1
    while True:
        offs = haystack.find(needle, offs+1)
        if offs == -1:
            break
        else:
            yield offs
text_file = open("scrape.txt","w")
html = urllib.request.urlopen("ENTER THE URL")
text = html.read()
print(text)
strtxt=str(text)
dbq1=[]
for offs in find_offsets(strtxt, '>'):
    dbq1.append(offs)
dbq2=[]
for offs in find_offsets(strtxt, '<'):
    dbq2.append(offs)
n1=len(dbq1)
n2=len(dbq2)
for i in range(0,n1):
    if(len(strtxt[dbq1[i]:dbq2[i+1]])>=5  and (strtxt[dbq1[i]:dbq2[i+1]]).count("\\t")==0 and (strtxt[dbq1[i]:dbq2[i+1]]).count(":")==0 and (strtxt[dbq1[i]:dbq2[i+1]]).count(";")==0 and (strtxt[dbq1[i]:dbq2[i+1]]).count("\"")==0 and (strtxt[dbq1[i]:dbq2[i+1]]).count("\\")==0):
        print((strtxt[dbq1[i]:dbq2[i+1]]).replace('>',''))
