import sys
from hlan.conf import hlanOption,hlanLog,MOD_DIR


def main(options,argvs,user='root',ip='127.0.0.1'):
    if options.runmode=='console':
        from ext.runConsole import runConsole
        hlanLog('runmode:控制台', Level=0, user=user, ip=ip)
        runConsole.main(options, argvs)
    elif options.runmode=='web':
        from ext.runFlask import runFlask
        hlanLog('runmode:http', Level=0, user=user, ip=ip)
        runFlask.main()
    elif options.runmode=='wechat':
        from ext.runWechat import runWechat
        hlanLog('运行方式:微信', Level=0, user=user, ip=ip)
        runWechat.main()
    else:
        #user自定义运行方式.按照接口规范
        hlanLog('运行方式错误:%s' % options.runmode,Level=2,user=user,ip=ip)
if __name__=='__main__':
    sys.path.append(MOD_DIR)
    parser=hlanOption()
    (options,args)=parser.parse_args(sys.argv)
    main(options,args)

   