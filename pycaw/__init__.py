import requests
import json

package_base = 'https://jlippold.github.io/tweakCompatible/json/packages/'
packages = 'https://jlippold.github.io/tweakCompatible/tweaks.json'
version_base = 'https://jlippold.github.io/tweakCompatible/json/iOS/'
versions = 'https://jlippold.github.io/tweakCompatible/json/iOSVersions.json'
repos = 'https://jlippold.github.io/tweakCompatible/json/repository-urls.json'
devices = 'https://jlippold.github.io/tweakCompatible/devices.json'


def err(message):
    raise Exception(message)

# Methods


def get(type, id=None, value=None):

    if type.lower() == 'package':
        try:
            if value != None:
                try:
                    o = requests.get(package_base + id + '.json').json()
                    e = json.dumps(o)
                    r = json.loads(e)

                    return r[value]
                except Exception:
                    err('Invalid value argument')

            return requests.get(package_base + id + '.json').json()
        except Exception:
            if id == None:
                err('Missing id argument')
            err('Invalid package ID')

    elif type.lower() == 'packages':
        return requests.get(packages).json()

    elif type.lower() == 'repos':
        return requests.get(repos).json()

    elif type.lower() == 'version':
        try:
            return requests.get(version_base + id + '.json').json()
        except Exception:
            if id == None:
                err('Missing id argument')
            err('Invalid iOS version')

    elif type.lower() == 'versions':
        return requests.get(versions).json()

    elif type.lower() == 'devices':
        return requests.get(devices).json()

    else:
        err('Invalid type argument')


def getIdFromName(name):
    o = requests.get(packages).json()
    e = json.dumps(o)
    r = json.loads(e)
    t = r['packages']

    for pkg in t:
        if pkg['name'].lower() == name.lower():
            return pkg['id']
