import requests
class api:
    def getv1pods(self):
        url = "http://192.168.9.137:8081/api/v1/pods"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    def getv1podsdefaultnamespace(self):
        url = "http://192.168.9.137:8081/api/v1/namespaces/default/pods/"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    def getlogs(self,podname):
        url = "http://192.168.9.137:8081/api/v1/namespaces/default/pods/{0}/log?tailLines=50&pretty=true".format(podname)
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text.encode('utf8')
#o  = api()
#o.getv1pods()