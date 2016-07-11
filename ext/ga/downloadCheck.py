from ext.ga.reqHTTP import mycurl
import threading
try: 
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET 

def RISING_CHECK(IP):
    global CURRENT_VERSION
    RISING_URL1='http://%s/rsupgrade/rspcver12.xml'%IP
    RISING_VERSION_CODE,RISING_VERSION_XML=mycurl(RISING_URL1)
    if RISING_VERSION_CODE!=200:
        return (RISING_VERSION_CODE,'','')
    root=ET.fromstring(RISING_VERSION_XML)
    RISING_VERSION_STATUS=''
    for i in root:
        C1=i.attrib
        try:
            RISING_VERSION=C1['VERSION']
            if CURRENT_VERSION==RISING_VERSION:
                RISING_VERSION_STATUS='OK'
            else:

                RISING_VERSION_STATUS=RISING_VERSION
        except:
            pass
        
    url='http://%s/rsupgrade/pcver/cms/compsver%s.inf'%(IP,RISING_VERSION)
    return (RISING_VERSION_CODE,RISING_VERSION_STATUS,mycurl(url)[0],RISING_VERSION)
def main(userLine,version):
    global CURRENT_VERSION
    CURRENT_VERSION=version
    T_thread=[]
    global res_json
    res_json={}
    for i in userLine:
        if i!='':
            t=threading.Thread(target=RISING_RES,args=(i,RISING_CHECK(i)))
            T_thread.append(t)
    for i in range(len(T_thread)):
        t.setDaemon(True)
        T_thread[i].start()
    for i in range(len(T_thread)):
        fina_flag=True
        if T_thread[i].is_alive():
            while fina_flag:
                if T_thread[i].is_alive():
                    continue
                else:
                    fina_flag=False
    return res_json
def RISING_RES(ip,res):
    global res_json
    if res[0]==0:
        res_json[ip]='网络错误'
    elif res[0]!=200:
        res_json[ip]='错误状态码%s'%res[0]
    else:
        if res[1]!='OK':
            res_json[ip]='当前版本%s与服务器不同步' %res[1]
        else:
            if res[2]!=200:
                res_json[ip]='没有最新版本配置文件'