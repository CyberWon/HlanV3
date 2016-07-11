from flask import Blueprint, render_template,request
from hlan import hlan,conf
from ext.ga import downloadCheck,packageCheck
from ext.ga.downloadCheck import RISING_CHECK
from ext.ga.packageCheck import GaIPGroup
ga_IPsCount=Blueprint('ga_IPsCount',__name__,template_folder='/templates')
ga_index=Blueprint('ga_index',__name__,template_folder='/templates')
ga_download_check=Blueprint('ga_download_check',__name__,template_folder='/templates')
ga_download_check_api=Blueprint('ga_download_check_api',__name__,template_folder='/templates')
MASTER_SERVER='192.168.10.100'
@ga_index.route('/ga')
def gaIndex():
    return render_template('ga/index.html')
@ga_IPsCount.route('/ga/IPsCount')
def gaIPsCount():
    return render_template('ga/ipscount.html')
@ga_IPsCount.route('/ga/IPsCount/api',methods=['GET', 'POST'])
def gaIPsCountApi():
    if request.args.get('m')=='t':
        ips=request.args.get('ips').split(';')
        res=hlan.main(module='gaIPsCount',args=ips)
        res_str='厂商\t\t\t安装数\t\t\t起始行\t\t\t结束行\n'
        for i in res:
            res_str+='%s\t\t\t%s\t\t\t%s\t\t\t%s\n'%(i,res[i]['ip_num'],res[i]['ip_start_line'],res[i]['ip_stop_line'])
        return '<pre>%s</pre>' % res_str
    elif request.args.get('m')=='g':
        return conf.execCMD(['sh','/tmp/tmp.sh'])
@ga_download_check.route('/ga/DownloadCheck')
def gaDownloadCheck():
    return render_template('ga/downloadcheck.html')
@ga_download_check_api.route('/ga/DownloadCheck/api',methods=['GET', 'POST'])
def gaDownloadCheckApi():
    if request.args.get('m')=='res':
        res_str='获取失败'
        li=request.form['ip'].split('\n')
        if request.args.get('c')=='rising':                  # 检测rising版本
                       
            res_str='IP\t\t\t\t\t故障原因\n'
            res=downloadCheck.main(li,request.args.get('d'))
            for i in res:
                res_str+='%s\t\t\t\t%s\n'%(i,res[i])
        else:
            res_str=packageCheck.main(li,request.args.get('c'),package_out=True,package_seg=request.args.get('d'))
        return '<pre>%s</pre>' % res_str
    elif request.args.get('m')=='info':
        if request.args.get('c')=='rising':
            res_str=RISING_CHECK(MASTER_SERVER)[3]
        else:
            res=packageCheck.main([MASTER_SERVER], request.args.get('c'))
            for i in res[MASTER_SERVER]:
                res_str='32:%s-64:%s'%(res[MASTER_SERVER][i]['32bit'][3],res[MASTER_SERVER][i]['64bit'][3])
        return res_str
    elif request.args.get('m')=='ipgroup':
        ip_group=GaIPGroup()
        return ip_group.getProvice(request.args.get('c')[1:])