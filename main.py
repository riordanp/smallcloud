from cloudapp.cloud import Cloud
from ConfigParser import SafeConfigParser
import sys

parser = SafeConfigParser()
parser.read('./smallcloud.conf')

mycloud = Cloud()
mycloud.auth(parser.get('auth', 'username'), parser.get('auth', 'password'))

print(sys.argv[1])
mycloud.upload_file(sys.argv[1])
