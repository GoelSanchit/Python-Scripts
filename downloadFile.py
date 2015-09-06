from urllib import requestl

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=6&e=18&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'

def download_any_file(csv_url):
    response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	dest_url = r'goog.csv'
	fx = open(dest_url,"w")
	for line in lines:
	    fx.write(line + "\n")
	fx.close()
	
download_any_file(goog_url)
		
    
