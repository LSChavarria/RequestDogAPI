import http.client
import json
conn = http.client.HTTPSConnection("dog.ceo")
payload = ''
headers = {
  'Cookie': '__cfduid=dbb7aba0e7895a88cd0d2a47d574e28911615683509'
}
conn.request("GET", "/api/breeds/list/all", payload, headers)
res = conn.getresponse()
data = res.read()
cadena1=data.decode("utf-8")
lista=json.loads(cadena1)

for each in lista:
    for i in lista[each]:
        if len(lista[each][i]) != 0:
            for j in lista[each][i]:
                print(i, j)
        else:
            print(i)