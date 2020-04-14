import requests, time
import json,sys
#from Config import Config ###############comment for unit test
from classes.Config import Config ########uncomment for unit test

class Token:
    def __init__(self):
        self.token = None
        self.config = Config()
        self.response = None
    
    def __url(self):
        return self.config.urlToken()

    def __proxy(self):
        return self.config.proxy()     

    def __body(self):
        return {'user': self.config.user(), 'password': self.config.passwd() }

    def __request(self):
        try:
            header = header = {'Content-type': 'application/json'}
            #resp = requests.post(self.__url(),proxies=self.__proxy(), json=self.__body(), headers=header)
            resp = requests.post(self.__url(), json=self.__body(), headers=header)
            self.response = resp.json()
            #print(resp.json())
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)

    def getToken(self):
        self.__request()
        dict_json = self.response
        if dict_json is not None:
            #print(str(dict_json))
            code = dict_json['Code']
            description = dict_json['Description']
            if code == 808:
                token = dict_json['Data']['token']
                return token
            else:
                return description
        else:
            return None


if __name__ == '__main__':
    w = Token()
    print(w.getToken())
    sys.exit(0)