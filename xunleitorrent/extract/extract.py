import re

def chunxiao_dns():
    url = 'http://www.chunxiao.tv'
    return url
def chunxiao_dianying_dns():
    url = 'http://www.chunxiao.tv/explore/dianying/p-'
    return url

def chunxiao_dianying(res):
    urls = re.findall(r'class="title".*?href="(.*?)"', res, re.S) # re.S 把文本信息转换成1行匹配
    return urls

def chunxiao_xiangqing(result):
    url = re.findall(r'class="dropdown".*?href="(.*?)"', result.text, re.S)

    lineurl = re.findall(r'(?<=class="bill active").*?href="(.*?)"', result.text, re.S)
    return {"url":url,"lineurl":lineurl}

def dianying_resource(result):
    file_name = re.findall(r'(?<=class="name hub">).*?(?=</a><div class="synopsis">)', result.text, re.S)

    file_content = re.findall(r'(?<=class="synopsis"><p>).*?(?=</p><a href=")', result.text, re.S)
    # <a href="javascript:;" class="more" style="display: inline;"><s></s>更多</a>
    file_url = re.findall(r'(?<=class="origin">).*?(?=<span class="copy")', result.text, re.S)
    return {'file_name':file_name, 'file_content':file_content, 'file_url':file_url}

def chunxiao_score(result):
    score = re.findall(r'(?<=class="score">).*?(?=</em>)', result.text, re.S)

    return score