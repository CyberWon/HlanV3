from ext.ga.reqHTTP import reqHeader
from hlan.conf import readGaIPGroup
import threading
class GaIPGroup():
    def __init__(self):
        self.ip_group=readGaIPGroup()
    def getIPGroup(self):
        return self.ip_group
    def getProvice(self,province='P1'):
        ip_str=''
        for i in self.ip_group[province]['ip']:
            ip_str+='%s\n'% i
        return ip_str
def campareSize(size_res,S32,S64):
    res_str=','
    res_staus=0
    try:
        if size_res['64bit'][0]!=200 or size_res['64bit'][0]!=200:
            return (1,'安装包不存在或网络错误')
        else:
            if size_res['64bit'][3]!=S64:
                res_staus=2
                res_str+='64位安装包有问题'
            if size_res['32bit'][3]!=S32:
                res_staus=3
                res_str+='32位安装包有问题'
    except Exception as e:
        res_staus=4
        res_str+='未知错误'
        print(e)
    return (res_staus,res_str[1:])
def packageCampare(package_res,package_seg):    
    P32_SIZE=package_seg.split('-')[0].split(':')[1]
    P64_SIZE=package_seg.split('-')[1].split(':')[1]
    res_campare='ip\t\t\t\t\t问题情况\n'
    for i in package_res:
        for k in package_res[i]:
            campare_res=(campareSize(package_res[i][k],P32_SIZE,P64_SIZE))
            if campare_res[0]!=0:
                res_campare+='%s\t\t\t\t%s\n'%(i,campare_res[1])
    return res_campare
def packageCheck(package_ip,package_index):
    global res
    pcl=['360','金山','江民','瑞星']
    package_32bit_url='http://%s/AVs/services/avsoftwareprofilesrv/install_packages/%s/32/setup.exe'%(package_ip,package_index)
    package_64bit_url='http://%s/AVs/services/avsoftwareprofilesrv/install_packages/%s/64/setup.exe'%(package_ip,package_index)
    res[package_ip][pcl[int(package_index)]]={'32bit':reqHeader(package_32bit_url),'64bit':reqHeader(package_64bit_url)}
def main(package_ip_list,package_index,package_out=False,package_seg=''):
    global res
    res={}
    res.clear()
    T_thread=[]
    for ip in package_ip_list:
        if ip!='':
            res[ip]={}
            t=threading.Thread(target=packageCheck,args=(ip,package_index))
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
    if package_out:
        return packageCampare(res,package_seg)
    else:
        return res
if __name__=='__main__':
    test=GaIPGroup()
    print(test.getIPGroup())