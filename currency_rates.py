#!/usr/bin/env python

"""
Author - RGK
Date - 04th February 2014

Ever felt that you need an API that gives you the currency exchange
rate of INR against USD or GBP in real time?

This Python script is the answer to the above question

The input to this script is obtained in the form of an XML file from an RSS feed
The RSS feed we use for getting the latest currency rates is - http://themoneyconverter.com/rss-feed/INR/rss.xml

The structure of this RSS feed looks like this
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Exchange Rates For Indian Rupee</title>
    <link>http://themoneyconverter.com/INR/Exchange_Rates_For_Indian_Rupee.aspx</link>
    <description>RSS Exchange Rate Feed for Indian Rupee</description>
    <lastBuildDate>Tue, 04 Feb 2014 16:45:10 GMT</lastBuildDate>
    <language>en-US</language>
    <copyright>Copyright: (C) The Money Converter, see http://themoneyconverter.com </copyright>
    <docs>http://themoneyconverter.com/RSSFeeds.aspx</docs>
    <ttl>61</ttl>
    <image>
      <title>Exchange Rates For Indian Rupee</title>
      <url>http://themoneyconverter.com/images/TheMoneyConverter_sml.jpg</url>
      <link>http://themoneyconverter.com/INR/Exchange_Rates_For_Indian_Rupee.aspx</link>
    </image>
    <item>
      <title>AED/INR</title>
      <link>http://themoneyconverter.com/INR/AED.aspx</link>
      <pubDate>Tue, 04 Feb 2014 16:45:08 GMT</pubDate>
      <description>1 Indian Rupee = 0.05873 United Arab Emirates Dirham</description>
      <category>Middle East</category>
    </item>
    <item>
      <title>ARS/INR</title>
      <link>http://themoneyconverter.com/INR/ARS.aspx</link>
      <pubDate>Tue, 04 Feb 2014 16:45:08 GMT</pubDate>
      <description>1 Indian Rupee = 0.12797 Argentine Peso</description>
      <category>South America</category>
    </item>
    ...
    ...
  </channel>
</rss>

Use CString to perform read / write operation of the XML rather than store
the contents of the RSS feed obtained in a temporary file and delete it later
after the operations are done

"""

# - Standard Python modules
import urllib2
import cStringIO
import re
from xml.dom import minidom, Node
from xml.dom.minidom import parseString


class CurrencyRates:
    def __init__(self):
        self.__rss_feed_url = r'http://themoneyconverter.com/rss-feed/INR/rss.xml'
        self.__xml = cStringIO.StringIO()
        self.__exchange_rates = {}
        self.__regex = re.compile('[0-9]\.[0-9]+')


    def read_rss_feed(self):
        url_obj = urllib2.urlopen(self.__rss_feed_url)
        for each_line in url_obj:
            self.__xml.write(each_line.strip())


    def parse_xml(self):
        dom_obj = parseString(self.__xml.getvalue())
        items = dom_obj.getElementsByTagName('item')
        for each_item in items:
            child_of_items = each_item.childNodes
            for each_child_of_item in child_of_items:
                if each_child_of_item.nodeType == Node.ELEMENT_NODE and each_child_of_item.nodeName == 'title':
                    country = each_child_of_item.childNodes[0].data.strip().split("/")[0]
                if each_child_of_item.nodeType == Node.ELEMENT_NODE and each_child_of_item.nodeName == 'description':
                    value = each_child_of_item.childNodes[0].data.strip().split("=")[1]
                    value = float(self.__regex.search(value).group().strip())
                    self.__exchange_rates[country] = value
        return self.__exchange_rates


if __name__ == '__main__':
    cObj = CurrencyRates()
    cObj.read_rss_feed()
    exchange_rates = cObj.parse_xml()
    print('The currency exchange rates are printed below')
    print('The interpretation is - "unit foreign currency : x Indian rupees"')
    import pprint
    pp = pprint.PrettyPrinter(indent=4, width=80)
    pp.pprint(exchange_rates)
