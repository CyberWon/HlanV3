from hlan.conf import hlanLog
from hlan import hlan
def main(argvs,user='root'):
    
    if argvs['options']=='update':
        hlanLog('更新 :%s' % argvs,user=user)
    elif argvs['options']=='execute':
        hlanLog(argvs,user=user)
        argvs['module']=argvs['argvs'][1]
        print(hlan.main(module=argvs['module'],argvs=argvs['argvs']))
    elif argvs['options']=='build':
        hlanLog('打包:%s' % argvs,user=user)
    else:
        hlanLog('action参数错误:%s' % argvs['options'],Level=2,user=user)