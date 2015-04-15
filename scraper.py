import urllib
import urllib2
url = 'https://iemweb.biz.uiowa.edu/pricehistory/PriceHistory_GetData.cfm'
values = [('Market_ID', '149'), ('Month', '11'), ('Year', '2008')]
data = urllib.urlencode(values)
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
html = response.read()
print response.getcode()
print html
