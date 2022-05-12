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
    defip = "8.8.8.8"
    tmpfile = "trace.tmp"
    regex = r"(\d*)\s{1,}(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\*\s*$)\s*([\d\,\w]*|)"
    site = input("target address (" + defip + "): ") or defip

    os.system(('traceroute -n -q 1 {} > ' + tmpfile).format(site))

    file = open(tmpfile, 'r')
    trace = str(file.read())
    file.close()
    os.remove(tmpfile)

    print("\nNo|     IP        |CN|  Region  |   City     |   ISP")

    items = re.findall(regex, trace)

    for item in items:
        id = item[0]
        ip = item[1]

        if ip.strip() != "*":
            info = ipinfo(ip)

            if info['success']:
                country = info["country_code"]
                region = info["region"]
                city = info["city"]
                isp = info["connection"]["isp"]
            else:
                country = "**"
                region = "***"
                city = "***"
                isp = "***"

            print("{} {} {} {} {} {}".format("{0:2}".format(id), "{0:<15}".format(ip), "{0:2}".format(country), "{0:10}".format(region)[0:10], "{0:12}".format(city)[0:12], "{0:14}".format(isp)[0:14]))
        else:
            print("{} {} ** ***********".format("{0:2}".format(id), "{0:<15}".format(ip)))

if __name__ == "__main__":
    main()