from __future__ import print_function
import httplib2
import os
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/slides.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/presentations.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Slides API Python Quickstart'

def url_to_presenationid(url)

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'slides.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def find_text(url):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('slides', 'v1', http=http)
    presentationText = []

    presentationId = url_to_presenationid(url)
    presentation = service.presentations().get(
        presentationId=presentationId).execute()
    slides = presentation.get('slides')
    for i, slide in enumerate(slides):
        elements = slide.get('pageElements')
        for element in elements:
            if "shape" in element:
                if "shape" in element:
                    shape = element.get('shape')
                    text = shape.get('text')
                    textElements = text['textElements']
                    writing = textElements[1]['textRun']
                    content = writing['content']
                    with open("slideTexts.txt", "a") as myfile:
                        myfile.write(content)
        # for element in elements:
        #     print json.dumps(element, sort_keys=True, indent=4)
    #     if slides.
        #        print('- Slide #{} contains {} elements.'.format(i + 1,
        #    len(slide.get('pageElements'))))

if __name__ == '__main__':
    main()
