import httpx

from lxml import etree

url = "https://@e04.sapucc.in.tum.de/odata/907/Inventory"
certificate_path = "cert.crt"

try:
    with httpx.Client() as client:
        response = client.get(url, follow_redirects=True, auth=('V_4', '123456'))
        response.raise_for_status()

        root = etree.fromstring(response.text)
        with open("response.xml", "wb") as f:
            f.write(etree.tostring(root, pretty_print=True))


except httpx.HTTPError as e:
    print(f"HTTP Error: {e}")
