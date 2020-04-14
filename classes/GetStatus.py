import requests
import json
#from Config import Config ####################comment for unit test
#from Token import Token#################comment for unit test
from classes.Config import Config ###########uncomment for unit test
from classes.Token import Token #######uncomment for unit test

class GetStatus:
    def __init__(self):
        self.response = None
        self.token = None
        self.config = Config()
        self.header = self.__header()

        
    def __token(self):
        w = Token()
        return w.getToken()

    def __header(self):
        auth_token = self.__token()
        header = {'Content-type': 'application/json','Authorization': 'Bearer ' + auth_token}
        return header

    def getResponse(self):
        dict_json = self.response
        if dict_json is not None:
            lstContatos = dict_json['Data']['contacts']
            lstResponses = []
            for values in lstContatos:
                row = values['input'] + ';' + values['status']
                lstResponses.append(str(row))
            return lstResponses
        else:
            return None

    def __url(self):
        return self.config.urlContact()

    def __proxy(self):
        return self.config.proxy()   

    def request(self,dict_nu_terminal):
        try:
            body = {'contacts':  dict_nu_terminal  }
            #print(self.header)
            #resp = requests.post(self.__url(),proxies=self.__proxy(), json=body, headers=self.header)
            resp = requests.post(self.__url(), json=body, headers=self.header)
            if not resp is None:
                if 'json' in resp.headers.get('Content-Type'):
                    self.response = resp.json()
                else:
                    print('Response content is not in JSON format.')
            else:
                print('Resp is None')
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
   



if __name__ == '__main__':
    #num_Sem_get_status = 21995508999
    #dict_test = ['21998838286', '21995508999']
    dict_test = ['47984527467','21998838286']
    w = GetStatus()
    #print(w.proxy())
    #print(w.proxies)
    #print(w.getToken())
    w.request(dict_test)
    json_data = w.getResponse()
    print(json_data)
