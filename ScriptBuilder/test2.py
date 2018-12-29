#!/usr/bin/python2
# -*- coding: utf-8 -*-
# Author  : yangwang
# @Time    : 2018/12/29 10:29
# @Author  : yangwang
# @Email   : 631197757@qq.com
# @File    : test2.py
# @Software: PyCharm

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import xmind
from xmind.core import workbook,saver
from xmind.core.topic import TopicElement
def creatXmindFile(data):
    module=[]
    for item in data:
        module.append(item['module'])
    module=list(set(module))
    print(module)
    w = xmind.load("test3.xmind") # load an existing file or create a new workbook if nothing is found
    s2=w.createSheet() # create a new sheet
    s2.setTitle("框架")
    r2=s2.getRootTopic()
    r2.setTitle("框架")

    for i in range(len(module)):
        t=TopicElement()
        t.setTitle(module[i])
        r2.addSubTopic(t)
    w.addSheet(s2) # the second sheet is now added to the workbook
    r2_topics=r2.getSubTopics() # to loop on the subTopics
    for topic in r2_topics:
        topic_name=topic.getTitle()
        print (topic_name)
        for item in data:
            if topic_name == item['module'] :
                index=topic.getIndex()
                t=TopicElement()
                content=item['caseId']+" "+'\n'+item['summary']
                t.setTitle(content)
                r2_topics[index].addSubTopic(t)

                summary=t.getTitle()
                for item in data:
                    if item['summary'] in summary:
                        t1=TopicElement()
                        content1=item['name']
                        t1.setTitle(content1)
                        t.addSubTopic(t1)

    xmind.save(w,"test3.xmind") # and we save
if __name__=='__main__':
    data=[{
        'name': 'testClickTheMenuButton',
        'caseId':  '01',
        'module': '书架',
        'summary': '多次开启关闭书架',
        }
    ,{
        'name': 'testSearchWordWithoutResult',
        'caseId':  '02',
        'module': '搜索',
        'summary': '搜索无结果'
    }]
    creatXmindFile(data)
