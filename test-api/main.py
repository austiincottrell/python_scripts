import requests

class test:
  def __init__(self, method: str, url: str, body={}, headers={}, params={} ):
    ## Store any other variables you want to pass on at the first call of the function
    self.method  = method
    self.url     = url
    self.params  = params
    self.body    = body
    self.headers = headers
  def put(self):
    return requests.put(self.url,data =self.body,params=self.params,headers=self.headers)
  def post(self):
    return requests.post(self.url,data =self.body,params=self.params,headers=self.headers)
  def get(self):
    return requests.get(self.url,data =self.body,params=self.params,headers=self.headers)
  def delete(self):
    return requests.delete(self.url,data =self.body,params=self.params,headers=self.headers)
  def request(self):
    m = self.method.upper()
    if m == "POST":
      return self.post()
    if m == "PUT":
      return self.put()
    if m == "GET":
      return self.get()
    if m == "POST":
      return self.post()


## Example [Sumo Logic Folder API](https://api.sumologic.com/docs/#tag/folderManagement)
# value = test("post","https://api.sumologic.com/api/v2/content/folders",body={"name": "Personal","parentId": "0000000001C41EF2"},).request()
# print(value)