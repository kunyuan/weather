#!/usr/bin/env python
import datetime
import forecastio
import requests
import json
import time

def main():
    """
    Run load_forecast() with the given lat, lng, and time arguments.
    """
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    print j, lat, lon

    api_key = "b6235f6d81011107eeedb7ac0e124019"

    forecast = forecastio.load_forecast(api_key, lat, lon)

    print "===========Currently Data========="
    print forecast.currently()
    print forecast.currently().time
    print forecast.currently().time+datetime.timedelta(seconds=-time.timezone)

    #take Daylight Saving Time (DST) into account
    is_dst = time.daylight and time.localtime().tm_isdst > 0
    utc_offset = - (time.altzone if is_dst else time.timezone)

    print forecast.currently().time+datetime.timedelta(seconds=utc_offset)

    print forecast.currently().summary

    print "===========Hourly Data========="
    by_hour = forecast.hourly()
    print "Hourly Summary: %s" % (by_hour.summary)

    for hourly_data_point in by_hour.data:
        print hourly_data_point

    # print "===========Daily Data========="
    # by_day = forecast.daily()
    # print "Daily Summary: %s" % (by_day.summary)

    # for daily_data_point in by_day.data:
        # print daily_data_point
        # print daily_data_point.sunriseTime

if __name__ == "__main__":
    main()
