from urllib2 import urlopen
from bs4 import BeautifulSoup
import ssl
from selenium import webdriver
import time
from pylab import *
import string

driver = webdriver.PhantomJS(executable_path=r'C:\FYS\DIV\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('https://www.oslobors.no/markedsaktivitet/#/details/OSEBX.OSE/overview')
"""
userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.148 Safari/537.36 Vivaldi/1.4.589.38'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen('https://www.oslobors.no/markedsaktivitet/#/details/OSEBX.OSE/overview', context=ctx)
"""
time.sleep(5)
pageSource = driver.page_source

siste = BeautifulSoup(pageSource, 'lxml')
#sisteList = siste.findAll('td',{'class':'LASTNZ_DIV'})
sisteList = siste.find('g',{'class':'highcharts-series highcharts-series-0'})

data_set = []
for sett in sisteList.findAll('path'):
    data_set.append(sett)

dat = str(data_set[0])

dat = dat.split(' ')

l = []

for t in dat:
    if t =='312':
        t = 'f'
    try:
        l.append(float(t))
    except ValueError:
        pass

x = zeros(int((len(l)/2.))+1)
y = zeros(int((len(l)/2.))+1)



for num in range(len(l)):
    if num % 2 == 0:
        x[num/2] = l[num]
    else:
        y[num/2] = l[num]

x = linspace(0,len(y), len(y))

#print y
figure()
plot(x[10:495],y[10:495])
show()

print y[0:20]

FFT = abs(fft(y[0:495]))

figure()
plot(x[10:len(FFT)/2],FFT[10:len(FFT)/2])
show()

driver.close()
#for last in sisteList:
#    print(last)
#lage try catch - format figure - lage funksjon