import urllib3
import subprocess
import re
import command
import requests
from bs4 import BeautifulSoup


def get_geolocation():
    try:
        response = subprocess.check_output(
            '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s'
        )
        lines = response[1].split('\n')
        geourl = 'https://maps.googleapis.com/maps/api/browserlocation/json?browser=firefox&sensor=true'
        for i in range(1, len(lines)):
            macs = re.compile('([^ ].+) ([^ ]+:[^ ]+:[^ ]+:[^ ]+:[^ ]+:[^ ]+) ([^ ]+)').findall(lines[i])
            name = macs[0][0]
            mac = macs[0][1]
            ss = macs[0][2]
            geourl += '&wifi=mac:%s%%7Cssid:%s%%7Css:%s' % (mac.replace(":", "-"), name.replace(" ", "%20"), ss)
        # look up google maps API for lat/lng
        http = urllib3.PoolManager()
        response = http.request('GET', geourl)
        html = BeautifulSoup(response.data.decode('utf-8'))
        lat = re.compile('"lat" : (.+),').findall(html)[0]
        lng = re.compile('"lng" : (.+)').findall(html)[0]
        return (lat, lng)
    except:
        print
        "no internet connection found, no location code!"
        return ('NULL', 'NULL')


print(get_geolocation())