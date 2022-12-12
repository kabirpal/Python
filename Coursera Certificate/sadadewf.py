import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'file:///C:/Users/kp534/Desktop/Python/googleapi/where.html?'

while True:
    address = input('Enter location:')
    if len(address)<1:break

    url = serviceurl + urllib.parse.urlencode(
          {'address':address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived', len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('===failure to reterive===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geomatery"]["location"]["lat"]
    lng = js["results"][0]["geomatery"]["location"]["lng"]
    print('lat',lat, 'lng',lng)
    location = js['results'][0]['formatted address']
    print(location)
