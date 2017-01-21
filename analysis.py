from __future__ import print_function
import json
import urllib2

import requests

try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
    from urllib.parse import urlencode
except ImportError:
    from urlparse import urlparse
    from urllib2 import urlopen
    from urllib import urlencode

def get_keywords(data):
    endpoint = '/text/TextGetRankedKeywords'
    analysis = analyse_text(data, endpoint)

    if (analysis['status'] != 'OK'): return []

    result = []
    for entry in analysis['keywords']:
        result.append(entry['text'])
    return result

def get_concepts(data):
    endpoint = '/text/TextGetRankedConcepts'
    analysis = analyse_text(data, endpoint)

    if (analysis['status'] != 'OK'): return []

    result = []
    for entry in analysis['concepts']:
        result.append(entry['text'])
    return result

def analyse_text(data, endpoint):

    s = requests.Session()
    # Add the API Key and set the output mode to JSON
    params = {}
    params['apikey'] = '956c2be77d854cfa78e2f5b678267624854a4ab3'
    params['outputMode'] = 'json'
    params['text'] = data
    # Insert the base url

    base_url = 'http://access.alchemyapi.com/calls'
    post_url = ""
    try:
        post_url = base_url + endpoint + \
            '?' + urlencode(params).encode('utf-8')
    except TypeError:
        post_url = base_url + endpoint + '?' + urlencode(params)
    analysis = ""
    try:
        analysis = s.post(url=post_url, data=bytearray())
    except Exception as e:
        print(e)
        return {'status': 'ERROR', 'statusInfo': 'network-error'}

    try:
        return analysis.json()
    except Exception as e:
        if analysis != "":
            print(analysis)
        print(e)
        return {'status': 'ERROR', 'statusInfo': 'parse-error'}



def get_phrases(file_name):
    # empty file that will be written into
    with open('keyWords.txt', 'w'):
        pass

    for line in open(file_name, 'r'):
        keywords = get_keywords(line)
        concepts = get_concepts(line)
        with open('keyWords.txt', 'a') as write_file:
            for word in keywords:
                if (word != keywords[0]): write_file.write(', ')
                write_file.write(word)
            for word in concepts:
                write_file.write(', ' + word)
            if (len(keywords) == 0 and len(concepts) == 0):
                write_file.write('NONE')
            write_file.write('\n')

def main():
    return 0

if __name__ == '__main__':
    main()
