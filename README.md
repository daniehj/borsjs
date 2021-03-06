# borsjs

A script for reading stockprices with ticker, uses PhantomJS

## Getting Started

Download file and install PhantomJS

### Prerequisites

For running borsjs you need:
Urllib2,
BeatifulSoup,
Selenium,
Pylab,

Also need PhantomJS installed



### Installing

To install the python modules:

```python
pip install urllib2, bs4, selenium, pylab
```

For the phantomJS module you need to download the driver from homepage, then set

```python
driver = webdriver.PhantomJS(executable_path=r'%PHANTOMJS_PATH\bin\phantomjs.exe')
```

Also need to set the path in the enviroment variable

## Usage

Write ticker in commmandline

```
>borsjs.py TEL
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
>borsjs.py OSEBX
Siste: 147.50
High: 734.45
Low: 730.53
```

And plots 3 plots:

![Full chart](https://github.com/daniehj/borsjs/raw/master/chartosebx.png)
![Histogram](https://github.com/daniehj/borsjs/raw/master/histosebx.png)
![FFT of full chart](https://github.com/daniehj/borsjs/raw/master/fftosebx.png)
