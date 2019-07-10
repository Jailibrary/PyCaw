from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

print(parser.get('urls', 'package_base'))
