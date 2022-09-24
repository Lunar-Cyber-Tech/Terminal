import requests, socket

class ip_resolver:
    def __init__(self, ip):
        self.ip = ip

    def resolve(self):
        if 'https://www.' in self.ip or 'http://www.' in self.ip or 'www.' in self.ip:
            self.ip = self.ip.replace('https://www.', 'www.')
            self.ip = self.ip.replace('http://www.', 'www.')
            self.ip = socket.gethostbyname(self.ip) # format the url
        r = requests.get(f'http://ip-api.com/json/{self.ip}')
        data = r.json()
        print(f'''
IP: {data['query']}
Country: {data['country']}
Region: {data['regionName']}
City: {data['city']}
Zip: {data['zip']}
ISP: {data['isp']}
Organization: {data['org']}
AS: {data['as']}
Latitude: {data['lat']}
Longitude: {data['lon']}
Timezone: {data['timezone']}''')
