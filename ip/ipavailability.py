import socket
import struct
import os
import json
from urllib.request import urlopen
import re

save = False
mdir = os.path.dirname(os.path.realpath(__file__)) + '/'
cachefile = mdir + 'ipcache.tmp'
ipres = {}
if os.path.isfile(cachefile):
    with open(cachefile) as f:
        ipres = json.load(f)

def ipinfo(ip):
    try:
        return dict(json.loads(urlopen('http://ipwho.is/' + str(ip)).read()))
    except Exception as e:
        return {'success': False}

def diap(start, end):
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end.strip()))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in
            range(start, end)]

def ping(ip):
    res = os.system('ping -c 1 -W 1 ' + ip + '>/dev/null')
    if res == 0:
        return True
    else:
        return False

ips = []
with open(mdir + 'ips.txt') as file:
    for line in file:
        if line.find(' - ') != -1:
            (start, end) = line.split(' - ')
            ips = ips + diap(start, end)
        else:
            ips.append(line)

print ('\nA|      IP        |  ASN  |      ISP       | Host')
regex = r"\d+\.\d+\.\d+\.\d+"
for ip in ips:
    ip = ip.strip()
    host = ''
    try:
        if not re.findall(regex, ip):
            host = ip
            ip = socket.gethostbyname(ip)
    except Exception as e:
        print ("\033[1;31m- " + ip + ' not associated')
        continue
    av = "\033[1;33m-"
    if ping(ip):
        av = "\033[1;32m+"

    asn = '-----'
    isp = '-----'

    if ip in ipres.keys():
        info = ipres[ip]
    else:
        save = True
        info = ipinfo(ip)
        ipres[ip] = info

    if info['success']:
        asn = info['connection']['asn']
        isp = info['connection']['isp']
        isp = re.sub(r"PRIVATE JOINT STOCK COMPANY", '', isp,
                     flags=re.IGNORECASE)

    print ('{} {} {} {} {}'.format(
        '{0:2}'.format(av),
        '{0:15}'.format(ip),
        '{0:8}'.format(asn),
        '{0:16}'.format(isp)[0:16],
        '{0:16}'.format(host)[0:16]
        ))

if save:
    with open(cachefile, 'w') as f:
        f.write(json.dumps(ipres))
