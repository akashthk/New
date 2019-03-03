import re

class WebsiteTreat:
    def __init__(self):
        self._domain  = ['.com','.co.uk','.ca','.com.au']

    def Extract_Core_URL_content(self,url):
        CoreURLlist = []
        for domain in self._domain:
            re_string = 'http[s]*:\/\/(.+?.)'+domain
            m = re.search(re_string, url)
            if m:
                found = m.group(1)
                found = re.sub('www.',"",str(found))

                return found
    def Extract_Core_URL(self,url):
        CoreURLlist = []
        for domain in self._domain:
            re_string = 'http[s]*:\/\/(.+?.)'+domain
            m = re.search(re_string, url)
            if m:
                found = m.group(0)
                found = re.sub('www.',"",str(found))
                found = re.sub('https://',"",str(found))
                found = re.sub('http://',"",str(found))
                return found
