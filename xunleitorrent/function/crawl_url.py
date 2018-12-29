#--**-*- coding:utf-8 -*-**--
import hashlib
import re,os
import time
import concurrent
from concurrent.futures import ThreadPoolExecutor

import requests
from extract import extract
from config.logger import logger

log = logger("crawl_url").getlog()
p=ThreadPoolExecutor(1) #创建1个程池中，容纳线程个数为30个；
log.info("启动线程池!!!")
# Thread.currentThread().setName(ThreadPoolFairEx.renameThread(Thread.currentThread(), this.threadName));

class crawl_url():
    def get_index(self,url):
        respose = requests.get(url)
        if respose.status_code==200:
            return respose.text

    def parse_index(self,res):
        time.sleep(2)
        res=res.result() #进程执行完毕后，得到1个对象
        urls = extract.chunxiao_dianying(res)
        if len(urls) == 0:
            log.error("没有获取到列表中的地址信息，直接返回！")
            return
        # <p class="summary">悬疑惊悚</p><em>6.7<s></s></em>
        # 资源列表class="title".*?href="(.*?)"
        i=0
        for url in urls:

            i= i + 1
            log.info(i)
            (down_url,score) = self.get_downurl(url)

            if len(score)>0 and float(score[0]) > 6:

                # log.info("获取目标资源评分:%s，提交到线程池。" % score)
                p.submit(self.get_detail(down_url,score))  #获取详情页 提交到线程池
            elif len(score)>0 and float(score[0]) <= 6:
                log.info("获取目标资源评分:%s,评分太低，不执行保存！！" % score)
            else:
                log.info("该网站地址下没有评分！！！！" )

    # 返回下载页的url
    def get_downurl(self,url):
        if not url.startswith('http'):
            log.info(extract.chunxiao_dns())
            url=extract.chunxiao_dns() + str(url)
        log.info("详情页地址：%s" % url)
        result = requests.get(url)

        if result.status_code==200 :

            url = extract.chunxiao_xiangqing(result)['url']
            log.info("下载页面的url：%s" % url)
            lineurl = extract.chunxiao_xiangqing(result)['lineurl']
            log.info("当下载地址不存在时使用在线地址：%s" % lineurl)
            time.sleep(2)
            score = extract.chunxiao_score(result)
            if len(url) > 0:
                url = extract.chunxiao_dns() + str(url[0])
                log.info("下载页目标地址：%s" % url)
                return url, score

            elif len(url) == 0:
                if len(lineurl) > 0:
                    url = extract.chunxiao_dns() + str(lineurl[0])
                    log.info("在线地址：%s" % url)
                    return url, score
                else:
                    log.info("在线地址不存在！！")
                    return
                # save(mp4_url)

    # 获取到目标资源，并提交保存
    def get_detail(self, url, score):
        #http://www.chunxiao.tv/
        # album/jiepoushilingyishijianzhinanshengxiushe
        result = requests.get(url)
        print(result.text)
        file_name = extract.dianying_resource(result)['file_name']
        if result.status_code==200 and len(file_name) != 0:
            file_content = extract.dianying_resource(result)['file_content']
            # <a href="javascript:;" class="more" style="display: inline;"><s></s>更多</a>
            file_url = extract.dianying_resource(result)['file_url']

            cotents = "获取目标资源名:%s" % file_name + '\n' + "获取目标资源评分: % s" % score + '\n' + \
                      "获取目标资源描述:%s" % file_content + '\n' + "获取目标资源地址:%s" % file_url
            self.save_txt(file_name[0],cotents)

    def save_txt(self,filename, contents):
        path = os.path.dirname(os.path.abspath('.')) + "/file/"
        filename = path + filename+ ".txt"
        fh = open(filename, 'w', encoding='utf-8')
        fh.write(contents)
        fh.close()

    def main(self):
        for i in range(2):
            # http://www.chunxiao.tv/explore/dianying/p-1
            time.sleep(3)
            log.info("影视资源列表第%s页：" % i)
            p.submit(self.get_index,extract.chunxiao_dianying_dns()+str(i) ).add_done_callback(self.parse_index)
            time.sleep(3)
            log.info(extract.chunxiao_dianying_dns()+str(i))

            #1、先把爬主页的任务（get_index）异步提交到线程池
            #2、get_index任务执行完后，会通过回调函add_done_callback（）数通知主线程，任务完成；
            #2、把get_index执行结果（注意线程执行结果是对象，调用res=res.result()方法，才能获取真正执行结果），当做参数传给parse_index
            #3、parse_index任务执行完毕后，
            #4、通过循环，再次把获取详情页 get_detail（）任务提交到线程池执行

if __name__ == '__main__':
    crawl_url = crawl_url()
    crawl_url.main()