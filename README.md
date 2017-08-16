# # borsjs

A script for reading stockprices with ticker, uses PhantomJS

## Getting Started

Download file and install PhantomJS

### Prerequisites

For running borsjs you need:
Urllib2
BeatifulSoup
Selenium
Pylab

Also need PhantomJS installed



### Installing

For installing the python modules you nedd

```
pip install urllib2, bs4, selenium, pylab
```

For the phantomJS module you need to download the driver from homepage, then set

```
driver = webdriver.PhantomJS(executable_path=r'%PHANTOMJS_PATH\bin\phantomjs.exe')
```

Also need to set the path in the enviroment variable

## Usage

Write ticker in commmandline

```
>borsjs.oy TEL
```

Or no ticker will give a list of tickers, then place ticker name

```
Use one of these tickers:

Tickerlist
.
.
.

Enter ticker:
ATEA
```


### Some screenshots and print example

Uses commandline-style

```
>borsjs.oy OSEBX
Siste: 147.50
High: 734.45
Low: 730.53

```

Screenshots

