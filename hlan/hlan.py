from hlan.conf import hlanLog
def main(**argvs):
    hlanLog(argvs, 0, user='', ip='')
    load_mod=__import__(argvs['module'])
    res=load_mod.main(argvs)
    return res  