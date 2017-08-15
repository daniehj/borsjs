from urllib2 import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from pylab import *

driver = webdriver.PhantomJS(executable_path=r'C:\FYS\DIV\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('https://www.oslobors.no/markedsaktivitet/#/details/OSEBX.OSE/overview')
#driver.get('https://www.oslobors.no/markedsaktivitet/#/details/ATEA.OSE/overview')

def bors():
    
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
        
    
    figure()
    title('Chart')
    plot(x[:count],360-y[:count])
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

bors()#for last in sisteList:
#    print(last)
#lage try catch - format figure - lage funksjon