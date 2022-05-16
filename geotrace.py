import socket
import sys
import os
import json
from urllib.request import urlopen
import re

def ipinfo(ip):
   try:
        return dict(json.loads(urlopen("http://ipwho.is/" + str(ip)).read()))
   except Except as e:
        return {"query":"".format(e), "success": false}

def main():
    save = False
    mdir = os.path.dirname(os.path.realpath(__file__)) + "/"
    defip = "8.8.8.8"
    cachefile = mdir + "ipcache.tmp"
    tmpfile = mdir + "trace.tmp"
    ipres = {}
    if os.path.isfile(cachefile):
        with open(cachefile) as f:
            ipres = json.load(f)

    regex = r"\n(\s+)?(\d+)\s+([0-9.]+|\*)"
    site = ""
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) < 5: continue
        site = sys.argv[i]
        break
    if not site:
        site = input("target address (" + defip + "): ") or defip
    if not re.findall(regex,site):
        site = socket.gethostbyname(site)

    os.system(('traceroute -n -q 1 {} > ' + tmpfile).format(site))

    file = open(tmpfile, 'r')
    trace = str(file.read())
    file.close()
    os.remove(tmpfile)

    print("\nNo|     IP        |CN|  Region  |   City     |   ISP")

    items = re.findall(regex, trace)

    for item in items:
        id = item[1]
        ip = item[2]

        country = "--"
        region = "-----"
        city = "-----"
        isp = "-----"

        if ip.strip() != "*":
            if ip in ipres.keys():
                info = ipres[ip]
            else:
                save = True
                info = ipinfo(ip)
                ipres[ip] = info

            if info['success']:
                country = info["country_code"]
                region = info["region"]
                city = info["city"]
                isp = info["connection"]["isp"]

        print("{} {} {} {} {} {}".format("{0:2}".format(id), "{0:15}".format(ip), "{0:2}".format(country), "{0:10}".format(region)[0:10], "{0:12}".format(city)[0:12], "{0:14}".format(isp)[0:14]))

    if save:
        with open(cachefile, 'w') as f:
            f.write(json.dumps(ipres))

if __name__ == "__main__":
    main()