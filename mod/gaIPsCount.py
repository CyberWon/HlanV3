import threading

def compareIP(ipv,ip_seg): 
    '''比较IP是不是属于这个IP段
    ip_seg这个是从文件里读取的IP段信息
    ipv：ip value 就是IP
    '''
    for i in ip_seg:  
        ip_seg_start,ip_seg_stop=i.split('-') #以-分割成列表，['起始IP','结束IP']
        ipt=ip_seg_start.split('.') #ip start: 将起始IP以.分割成列表['192','168','0','1']
        ipp=ip_seg_stop.split('.')#ip stop: 将起始IP以.分割成列表['192','168','0','255']
        ip=ipv.split('.')#ip: 将IP以.分割成列表['192','168','0','2']
        for x in range(4): #用来定位IP段不同部分的下标。比如。10.1.x.x-10.2.x.x,会被看作下表1，
            if ipt[x]!=ipp[x]:  # 判断相同下标不同的部分。
                if ip[x-1]==ipp[x-1]: #判断前一位。避免iP段是10.1.x.x -10.2.x.x 但是IP是9.1.x.x
                    if int(ip[x])>=int(ipt[x]) and int(ip[x])<=int(ipp[x]): # 判断IP是不是大于等于起始，小于等于结束
                        return True #满足时候返回true
                break #前一位不同没必要继续这次循环了。所以中中断。让上一层循环继续执行
    return False 
# def main(argvs):
#     ip_txt = open("/tmp/360.txt")
#     ip_seg=argvs['args']
#     ip_num=0
#     ip_line=0
#     ip_start_line=0
#     ip_stop_line=0
#     while 1:
#         lines = ip_txt.readlines(100000)
#         if not lines:
#             break
#         for line in lines:
#             ip_line+=1
#             if compareIP(line.split(',')[0],ip_seg):
#                 ip_num+=1
#                 if ip_start_line==0:
#                     ip_start_line=ip_line
#                 ip_stop_line=ip_line
#     return ('江民',ip_num,ip_start_line,ip_stop_line)      
def IPCount(company,ip_seg):
    global res
    if company=='瑞星':
        ip_txt = open("/tmp/ruixing.txt")
    elif company=='江民':
        ip_txt = open("/tmp/jiangmin.txt")
    elif company=='360':
        ip_txt = open("/tmp/360.txt")
    elif company=='金山':
        ip_txt = open("/tmp/jinshan.txt")
    else:
        ip_txt = open("test.txt")
    ip_num=0
    ip_line=0
    ip_start_line=0
    ip_stop_line=0
    
#     print compareIP('10.2.66.53',ip_seg)
    while 1:
        lines = ip_txt.readlines(100000)
        if not lines:
            break
        for line in lines:
            ip_line+=1
            if compareIP(line.split(',')[0],ip_seg):
                ip_num+=1
                if ip_start_line==0:
                    ip_start_line=ip_line
                ip_stop_line=ip_line
    res[company]={'ip_num':ip_num,'ip_start_line':ip_start_line,'ip_stop_line':ip_stop_line}
def main(argvs):
    T_thread=[]
    global res
    res={}
    company=('瑞星','360','江民','金山')
    for c in company:
        t=threading.Thread(target=IPCount,args=(c,argvs['args']))
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
    return res