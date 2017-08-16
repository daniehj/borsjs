from urllib2 import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from pylab import *
import sys



tickers = ['AFG','AKER','AKERBP','AKSO','ASETEK','ATEA',
 'AXA','B2H','BAKKA','DNB','DNO','EKO','ENTRA',
 'EPR','FRO','GIG','GJF','GOGL','GSF','HEX','IDEX',
 'KIT','KOA','KOG','LSG','LINK','MHG','NEXT','NANO',
 'NOD','NHY','NAS','NPRO','OLT','OPERA','ORK','PGS',
 'PHO','REC','SALM','SSO','SCHA','SCHB','SDRL','SRBANK',
 'STL','SNI','STB','SUBC','TEL','TGS160','THIN','TOM',
 'TRE','VEI','WWL','WEIFA','WWI','WWIB','XXL','YAR']

try:
    ticker = sys.argv[1]
except IndexError:
    print "Use one of these tickers:\n"
    for ticker in tickers:
        print ticker
    ticker = raw_input('\nEnter ticker:\n')
        

if ticker in tickers:
    
    site = 'https://www.oslobors.no/markedsaktivitet/#/details/%s.OSE/overview' % ticker
    
    driver = webdriver.PhantomJS(executable_path=r'C:\FYS\DIV\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    
def bors(site):
    
    driver.get(site)
    time.sleep(5)
    pageSource = driver.page_source
    
    page = BeautifulSoup(pageSource, 'lxml')
    
    
    try:
        chart = page.find('g',{'class':'highcharts-series highcharts-series-0'})
        siste = page.find('td',{'class':'number LASTNZ_DIV'})
        high = page.find('td',{'class':'number HIGH'})
        low = page.find('td',{'class':'number LOW'})
    except ValueError:
        bors()
    
    siste = siste.get_text()
    siste = float(siste.replace(',','.'))
    high = high.get_text()
    high = float(high.replace(',','.'))
    low = low.get_text()
    low = float(low.replace(',','.'))
    
    diff = high-low
    
    
    
    
    print """Siste: %.2f\nHigh: %.2f\nLow: %.2f""" % (siste,high,low)
    
    
    data_set = []
    for sett in chart.findAll('path'):
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
    y = zeros(len(x))
    
   
    
    for num in range(len(l)):
        if num % 2 == 0:
            x[num/2] = l[num]
        else:
            y[num/2] = l[num]
            
    
    count = 0
    i = 0
    while i <= len(x):
        if x[i] > x[i+1]:
            count = i
            break
        else:
            pass
        i += 1
        
    figname = 'Chart for %s' % ticker
    print diff
    figure()
    title(figname)
    plot(x[:count],high-y[:count]*(3./360))
    grid(True)
    show()
    
    #print y[0:20]
    
    FFT = abs(fft(y[0:count]))
    
    figure()
    title('FFT of the chart')
    plot(x[1:len(FFT)/2],FFT[1:len(FFT)/2])
    grid(True)
    show()
    
    driver.close()

bors(site)#for last in sisteList:
#    print(last)
#lage try catch - format figure - lage funksjon