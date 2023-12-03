import requests

from lxml import etree

url = "https://@e04.sapucc.in.tum.de/odata/907/Inventory"
certificate_path = "cert.crt"

response = requests.get(url, auth=('V_4', '123456'), verify=certificate_path)

print(response.text)
