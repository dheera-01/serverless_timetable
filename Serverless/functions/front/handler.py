import requests

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    rollnum = 'C' + req
    existCheck = requests.get("http://gateway.openfaas:8080/function/fetch",data=rollnum)
    if existCheck.text == "YES":
        return requests.get("http://gateway.openfaas:8080/function/timetable",data=req).text
    return "NO"
