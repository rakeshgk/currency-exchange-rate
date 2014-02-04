currency-exchange-rate
======================

An API which gives the value of Indian Rupee versus some of the other currencies around the world

Based on the data available from the RSS feed - http://themoneyconverter.com/rss-feed/INR/rss.xml

Parses the XML file and returns a dictionary which looks like this

The interpretation is - "unit foreign currency : x Indian rupees"

    {   u'AED': 0.05873,
        u'ARS': 0.12797,
        u'AUD': 0.01793,
        u'AWG': 0.02863,
        u'BAM': 0.02317,
        u'BBD': 0.03198,
        u'BDT': 1.24179,
        u'BGN': 0.02317,
        u'BHD': 0.00601,
        u'BMD': 0.01599,
        u'BOB': 0.11047,
        u'BRL': 0.03861,
        u'BSD': 0.01599,
        u'CAD': 0.01769,
        u'CHF': 0.01449,
        u'CLP': 8.92444,
        u'CNY': 0.09691,
        u'COP': 2.63529,
        ...}

How to use the API?

a. Create an object of the class - CurrencyRates

    cObj = CurrencyRates()

b. Call the read_rss_feed method

    cObj.read_rss_feed()

c. Store the dictionary returned by parse_xml

    exchange_rates = cObj.parse_xml()

d. Lastly, Don't forget to switch on the Internet!! You can look at the main method in the script if this is not helping you with the API usage
