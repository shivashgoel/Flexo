from apis import v1Pods
class getallpods:
    @staticmethod
    def getpods():
        o = v1Pods.api()
        result = o.getv1podsdefaultnamespace()
        result = dict(result)
        #print(result)
        totalpods = len(result['items'])
        poddetails = []
        for i in range(0, totalpods):
            name = result['items'][i]['metadata']['name']
            #print(o.getlogs(podname=name))
            poddetails.append({'name':result['items'][i]['metadata']['name'],'phase':result['items'][i]['status']['phase'],'image':result['items'][i]['status']['containerStatuses'][0]['image'],"logs": o.getlogs(podname=name)})
            #print(result['items'][i]['metadata']['name'], "\t\t\t", result['items'][i]['status']['phase'], "\t\t\t",
            #     result['items'][i]['status']['containerStatuses'][0]['image'])
        return poddetails





