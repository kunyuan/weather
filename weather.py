#!/usr/bin/env python
import datetime
import forecastio
import requests
import json
import time
import os

def main():
    """
    Run load_forecast() with the given lat, lng, and time arguments.
    """
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    # print j, lat, lon

    api_key = "b6235f6d81011107eeedb7ac0e124019"

    forecast = forecastio.load_forecast(api_key, lat, lon)

    #take Daylight Saving Time (DST) into account
    is_dst = time.daylight and time.localtime().tm_isdst > 0
    utc_offset = - (time.altzone if is_dst else time.timezone)

    print forecast.currently().time+datetime.timedelta(seconds=utc_offset)
    print "weather condition: ", forecast.currently().summary
    # os.system("/home/osmc/weather/codesend 3554818 -l 285")
    if "cloudy" in forecast.currently().summary:
        print "Send Turn On"
        os.system("/home/osmc/weather/codesend 3554824 -l 285")

    # outlet 1
    # "on" => 3554824,
    # "off" => 3554822
    # outlet 2
    # "on" => 3554818,
    # "off" => 3554817
    # outlet 3
    # "on" => 3554829,
    # "off" => 3554819

    # print "===========Daily Data========="
    # by_day = forecast.daily()
    # print "Daily Summary: %s" % (by_day.summary)

    # for daily_data_point in by_day.data:
        # print daily_data_point
        # print daily_data_point.sunriseTime

if __name__ == "__main__":
    main()
