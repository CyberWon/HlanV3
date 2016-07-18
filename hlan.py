import sys
from hlan.conf import hlanOption,hlanLog,MOD_DIR,reqRunmode
from hlan import hlan


def main(options,argvs,user='root',ip='127.0.0.1'):
    runmode=reqRunmode(options.runmode)
    if runmode != 'null':
        hlan.main(module=runmode,options=options.action,argvs=argvs)
    else:
        print('运行方式错误')
if __name__=='__main__':
    sys.path.append(MOD_DIR)
    parser=hlanOption()
    (options,args)=parser.parse_args(sys.argv)
    main(options,args)

   