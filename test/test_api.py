from lib.api import API

def test_request():
    request_url = "https://www.google.com/"
    request = API.request(request_url)
    
    assert request.status_code == 200
    assert request.url == request_url
    assert len(request.text) > 0

def test_find():
    request_url = "https://www.google.com/"
    request = API.request(request_url).text
    
    assert API.find(request, "<title>", "</title>") == "Google"
