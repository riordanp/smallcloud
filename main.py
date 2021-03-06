#!/usr/bin/python2

from cloudapp.cloud import Cloud
from ConfigParser import SafeConfigParser
import argparse
import os
import xerox

argparser = argparse.ArgumentParser(description='Cloudapp Uploader')
argparser.add_argument('-u', '--upload', help='Filename to upload', required=True)
args = argparser.parse_args()
confparser = SafeConfigParser()
confparser.read(os.path.abspath(os.path.join(os.path.dirname(__file__), './smallcloud.conf')))

mycloud = Cloud()
mycloud.auth(confparser.get('auth', 'username'), confparser.get('auth', 'password'))

print('Uploading ' + args.upload + '...')
mycloud.upload_file(args.upload)
xerox.copy(mycloud.list_items(page=1, per_page=1)[0]['url'])
print('Upload Successful. Copied link to clipboard.')
