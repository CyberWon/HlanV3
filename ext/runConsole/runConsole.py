from hlan.conf import hlanLog
from hlan import hlan
def main(options,argvs,user='root'):
    
    if options.action=='update':
        hlanLog('更新 :%s' % argvs,user=user)
    elif options.action=='execute':
        hlanLog(argvs,user=user)
        
        print(hlan.main(module='shell',args=('my','disk','src','dst')))
    elif options.action=='build':
        hlanLog('打包:%s' % argvs,user=user)
    else:
        hlanLog('action参数错误:%s' % options.action,Level=2,user=user)