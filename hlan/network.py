import json
from ext.ga import reqHTTP
class saltAPI:
    def __init__(self):
        self.__url = 'https://192.168.186.134:8888'   
        self.__user =  'admin'           
        self.__password = 'zabbix'         
        self.__token_id = self.salt_login()
 
    def salt_login(self):
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        encode = urllib.urlencode(params)
        obj = urllib.unquote(encode)
        headers = {'X-Auth-Token':''}
        url = self.__url + '/login'
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        try:
            token = content['return'][0]['token']
            return token
        except KeyError:
            raise KeyError
 
    def postRequest(self, obj, prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token'   : self.__token_id}
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        return content['return']
 
    def saltCmd(self, params):
        obj = urllib.urlencode(params)
        obj, number = re.subn("arg\d", 'arg', obj)
        res = self.postRequest(obj)
        return res
class zabbixAPI:
    def __init__(self):
        self.__url = 'http://zabbix.hlan.my/api_jsonrpc.php'    
        self.__user =  'admin'            
        self.__password = 'zabbix'        
        self.__token_id = self.zabbix_login()
 
    def zabbix_login(self):
        data = json.dumps({"jsonrpc": "2.0","method": "user.login","params": {"user": self.__user,"password": self.__password},"id": 0})
        headers = {"Content-Type":"application/json"}
        try:
            res=json.loads(reqHTTP.Post(self.__url, data, headers))
            return res['result']
        except Exception as e:
            print(e)
            return None
        
    def zabbix_api(self,method,params):
        data = json.dumps({"jsonrpc": "2.0","method": method,"params": params,"auth":self.__token_id,"id": 0})
        headers = {"Content-Type":"application/json"}
        try:
            res=json.loads(reqHTTP.Post(self.__url, data, headers))
            return res['result']
        except Exception as e:
            print(e)
if __name__=='__main__':
    zabbix=zabbixAPI()
    print(zabbix.zabbix_api("hostgroup.get",{"output":["groupid","name"]}))