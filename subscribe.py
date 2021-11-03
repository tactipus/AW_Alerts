import requests as rq
import pycurl as pc
import simplejason as json

#email = input("Please enter your email address: ")

URL = "https://www.niko-alzate.com/home.html"

payload = "say=Hi&to=Mom"

data = json.dumps("say=Hi&to=Mom")

response = rq.post(url=URL, data=payload)
print(response.status_code)
print(response.headers)

c = pc.Curl()
c.setopt(c.URL, "https://www.niko-alzate.com/home.html")
c.setopt(c.POSTFIELDS, data)
c.setopt(c.VERBOSE, True)

for i in range(100):
    c.perform()