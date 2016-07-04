from flask import Blueprint, render_template,request
from hlan import hlan
ga_IPsCount=Blueprint('ga_IPsCount',__name__,template_folder='/templates')
ga_index=Blueprint('ga_index',__name__,template_folder='/templates')
ga_download_check=Blueprint('ga_download_check',__name__,template_folder='/templates')
ga_download_check_api=Blueprint('ga_download_check_api',__name__,template_folder='/templates')
@ga_index.route('/ga')
def gaIndex():
    return render_template('ga/index.html')
@ga_IPsCount.route('/ga/IPsCount')
def gaIPsCount():
    return render_template('ga/ipscount.html')
@ga_IPsCount.route('/ga/IPsCount/api',methods=['GET', 'POST'])
def gaIPsCountApi():
    ips=request.args.get('ips').split(';')
    res=hlan.main(module='gaIPsCount',args=ips)
    res_str='厂商\t\t\t安装数\t\t\t起始行\t\t\t结束行\n'
    for i in res:
        res_str+='%s\t\t\t%s\t\t\t%s\t\t\t%s\n'%(i,res[i]['ip_num'],res[i]['ip_start_line'],res[i]['ip_stop_line'])
    return '<pre>%s</pre>' % res_str
@ga_download_check.route('/ga/DownloadCheck')
def gaDownloadCheck():
    return render_template('ga/downloadcheck.html')
@ga_download_check_api.route('/ga/DownloadCheck/api',methods=['GET', 'POST'])
def gaDownloadCheckApi():
    from ext.ga import downloadCheck 
    if request.args.get('c')=='2':
        li=request.form['ip'].split('\n')
        res_str='IP\t\t\t\t\t故障原因\n'
        res=downloadCheck.main(li)
        for i in res:
            res_str+='%s\t\t\t\t%s\n'%(i,res[i])
    else:
        print(request.args.get('c'))
    return '<pre>%s</pre>' % res_str