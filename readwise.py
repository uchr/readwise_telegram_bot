import requests,sys
#proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
class ReadWise:
    def __init__(self, token):
        self.token = token


    def check_token(self):
        r = requests.get(url="https://readwise.io/api/v2/auth/",headers={"Authorization": "Token %s" % self.token})
        if r.status_code != 204:
            sys.exit("[+] Readwise token is outdated. Cannot continue working.")


    def save(self, **kwargs):
        # if smth is empty in the telegram post send empty string to Readwise 
        for v in kwargs.values():
            if v is None:
                v = ""
        r = requests.post(url="https://readwise.io/api/v3/save/",headers={"Authorization": "Token %s" % self.token},
        json=
            {
            "url": kwargs.get("url"),
            "html": kwargs.get("html"),
            "title": kwargs.get("title"),
            "summary": kwargs.get("summary"),
            "should_clean_html": "true"
            }

        )
    