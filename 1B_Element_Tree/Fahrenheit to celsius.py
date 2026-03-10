import requests
import xml.etree.ElementTree as ET

url = "https://www.w3schools.com/xml/tempconvert.asmx"

temp = float(input("Enter a temp in fahrenheit: "))

SOAPEnvelope = f"""
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="https://www.w3schools.com/xml/">
<soap:Body>
<FahrenheitToCelsius>
</soap:Body>
</soap:Envelope>
"""

headers = {
"Content-Type": "text/xml; charset=utf-8",
"SOAPAction": "https://www.w3schools.com/xml/FahrenheitToCelsius"
}

response = requests.post(url, data=SOAPEnvelope, headers=headers)

root = ET.fromstring(response.text)

for child in root.iter("{https://www.w3schools.com/xml/tempconvert.asmx?op=FahrenheitToCelsius}Result"):
    c2f = child.text

print(f"{temp} is equal to {c2f}°F")