# -*- coding: utf-8 -*-

from excle_processor import excle_pro,get_ExcleContent
from excle_processor import settings
from db_processor import db_processor
class run(object):
    def __init__(self):
        self.db = db_processor()
        self.titel = excle_pro()


    def start(self):
        def tt(j,setting,c):
            x = 0
            y = 10
            # 0\1\2\3
            print("标题%s，%s，%s"%(j,setting,c))
            exc_con = get_ExcleContent(c)
            if None is not setting and '' is not setting:
                SQL = setting[0]
                # print(exc_con[0])
                for ic in range(1,len(exc_con[0])):
                    result = self.db.select_table(SQL % exc_con[0][ic])
                    # print('result',result)
                    exc_c = exc_con[2][ic]
                    try:
                        if None is not result:
                            eec = exc_c[y*(c-1):y*c]
                            print(eec)
                            for p in range(2,len(eec)):

                                if float(result[p - 2]) == eec[p] :
                                    print("表名称：%s，数据库中数据为：%s,excle中的数据为：%s,通过" % (j,float(result[p - 2]), exc_c[p]))
                                else:
                                    print("表名称：%s，数据库中数据为：%s,excle中的数据为：%s,不通过" % (j,float(result[p - 2]), exc_c[p]))
                    except Exception as e:
                        print(e)
                # # TABLENAME = setting[1]
                # #__ROW = setting[2]
                #     print(result)
                # LEN = len(self.titel)

        # for i in range(len(self.titel)):
        c = 0
        for i in self.titel:
            c= c + 1
            # for c in range(len(self.titel)):
            t = settings(i)
            if t is False:
                pass
            else:
                tt(i, t,c)
            # else:

    # 配置中有多个表名，有过个sql配置，有一些可能是无效的，当有无效配置报错拒绝或者跳到相应的配置中比较，返回对应文档的配置结果

if __name__ == '__main__':
    run = run()
    run.start()