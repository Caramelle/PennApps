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



def url_to_presenationId(url):
    parts = url.split('/')
    return parts[5]


def get_credentials():

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/slides.googleapis.com-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/presentations'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Slides API Python Quickstart'

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

    presentationId = url_to_presenationId(url)
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

def add_image(url, image_url, page_id):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('slides', 'v1', http=http)

    presentationId = url_to_presenationId(url)
    requests = []
    image_id = 'MyImage_01'
    emu4M = {
        'magnitude': 4000000,
        'unit': 'EMU'
    }
    requests.append({
        'createImage': {
            'objectId': image_id,
            'url': image_url,
            'elementProperties': {
                'pageObjectId': page_id,
                'size': {
                    'height': emu4M,
                    'width': emu4M
                },
                'transform': {
                    'scaleX': 1,
                    'scaleY': 1,
                    'translateX': 100000,
                    'translateY': 100000,
                    'unit': 'EMU'
                }
            }
        }
    })

    # Execute the request.
    body = {
        'requests': requests
    }
    response = service.presentations().batchUpdate(presentationId=presentationId,
                                                          body=body).execute()
    create_image_response = response.get('replies')[0].get('createImage')
    print('Created image with ID: {0}'.format(create_image_response.get('objectId')))

add_image("https://docs.google.com/presentation/d/1BUUh7a92Smqvis_ht0XZZl9BqwKfKkkpUTn9F9Fo8no/edit", "http://media0.giphy.com/media/26uffErnoIpeQ3PmU/200_d.gif", 0)
