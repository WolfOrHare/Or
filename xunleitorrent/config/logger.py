import logging,os,time

class logger(object):

    def __init__(self,logger):
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #
        rq = time.strftime("%Y%m%d%H",time.localtime(time.time()))
        logpath = os.path.dirname(os.path.abspath('.'))+"/logs/"
        logname = logpath+rq+".log"
        # print(logname)

        # 创建一个handler，写入日志文件到磁盘
        fh = logging.FileHandler(logname)
        fh.setLevel(logging.INFO)

        #再创建一个handler，输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler 输出格式,参数内容是固定格式
        formattter = logging.Formatter('%(asctime)s---->%(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formattter)
        ch.setFormatter(formattter)

        #将handler添加给logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger