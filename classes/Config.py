import json

class Config:

    DEFAULT_CONFIGFILE = 'config.json'

    def __init__(self, configfile=DEFAULT_CONFIGFILE):
        self.configfile = configfile
        self.configure() 

    def configure(self):
        try:
            with open(self.configfile, 'r') as configfile_contents:
                self.config = json.load(configfile_contents)
        except:
            print("WARN: ")
            self.config = {}
    
    def urlToken(self):
        if self.config is not None:
            return self.config['SERVICE']['TOKEN_URL']

    def urlContact(self):
        if self.config is not None:
            return self.config['SERVICE']['CONTACT_URL']
            
    def user(self):
        if self.config is not None:
            return self.config['SERVICE']['USER']
            
    def passwd(self):
        if self.config is not None:
            return self.config['SERVICE']['PASSWORD']

    def proxy(self):
        if self.config is not None:
            user  = self.config['PROXY']['USER']
            password  = self.config['PROXY']['PASSWORD']
            proxy  = self.config['PROXY']['ADDRESS']
            port  = self.config['PROXY']['PORT']
            return {
                'http': 'http://'+ user + ':'+ password +'@' + proxy +':' + port,
                'https': 'https://'+ user + ':'+ password +'@' + proxy +':' + port,
            }
            

if __name__ == '__main__':
    conf = Config()
    conf.configure()
    print(conf.urlToken())
    print(conf.user())
    print(conf.passwd())
    print(conf.proxy())
    print(conf.urlContact())