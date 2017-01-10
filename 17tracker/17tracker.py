#!/usr/bin/python
import requests
import argparse


class Tracker(object):

    tracker_url = 'http://www.17track.net/restapi/handlertrack.ashx'

    headers = {
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.17track.net',
    'Referer': 'http://www.17track.net/pt/track?nums={package}&fc=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }

    form_data = '{{"guid":"","data":[{{"num":"{package}"}}]}}'


    def __init__(self):
        self.session = requests.Session()


    def format_entry(self, entry):
        return '{package} - {date} - {location} - {message}'.format(**entry)


    def track(self, package):
        lheaders = self.headers
        lheaders['Referer'] = lheaders['Referer'].format(package=package)
        lform = self.form_data.format(package=package)
        r = self.session.post(self.tracker_url, headers=lheaders, data=lform)

        d = {}
        data = r.json()
        for k in data['dat']:
            d['package'] = k['no']
            d['last_event'] = {}
            d['last_event']['package'] = d['package']
            d['last_event']['date'] = k['track']['z0']['a']
            d['last_event']['location'] = k['track']['z0']['c']
            d['last_event']['message'] = k['track']['z0']['z']

            d['all_events'] = []
            for event in k['track']['z1']:
                o = {}
                o['package'] = d['package']
                o['date'] = event['a']
                o['location'] = event['c']
                o['message'] = event['z']
                d['all_events'].append(o)
        return d

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Track any package on 17Track.net')
    parser.add_argument('packages', type=str, action='append', help='packages to track')
    args = parser.parse_args()

    t = Tracker()
    for p in args.packages:
        print(t.format_entry(t.track(p)['last_event']))










