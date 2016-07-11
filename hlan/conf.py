import os,yaml,subprocess

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
MOD_DIR = os.path.join(BASE_DIR,'mod')
EXT_DIR = os.path.join(BASE_DIR,'ext')
def hlanOption():
    from optparse import OptionParser 
    parser = OptionParser()
    parser.add_option("-a", "--action", dest="action",
                      help="设置执行的动作  update=更新 build:打包 *execute:执行模块", 
                      default="execute",metavar="execute")
    parser.add_option("-r", "--run", dest="runmode",
                      help="设置启动的方式  *console=控制台 web:http wechat:微信", 
                      default="console",metavar="console")
    parser.add_option("-d", "--daemon", dest="daemon",
                      help="作为服务启动  True/*False", 
                      default=False,metavar="False")
    return parser
def hlanLog(msg,Level=0,user='root',ip='127.0.0.1'):
    '''
    0: info : 信息
    1: warning :警告
    2: error : 错误
    '''
    import logging 
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/tmp/hlan.log',
                filemode='a')
    if Level==0:
        logging.info('%s %s %s'%(ip,user,msg))
    elif Level==1:
        logging.warn('%s %s %s'%(ip,user,msg))
    elif Level==2:
        logging.error('%s %s %s'%(ip,user,msg))
def readGaIPGroup():
    with open(os.path.join(BASE_DIR,'etc/ga/ip_group.yml'),'r') as f:
        ga_ip_group=yaml.load(f)
    return ga_ip_group
def execCMD(f):
    return subprocess.call(f)