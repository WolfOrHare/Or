#--**-*- coding:utf-8 -*-**--

import base64
def download_address_translation(original_address):
    original_address = str(original_address)
    if "thunder://" in original_address:
        original_address = original_address.replace('thunder://', '')
        original_address = base64.b64decode(original_address)
        original_address = original_address.decode('gbk')
        original_address = original_address[2:len(original_address)-2]

        result = original_address.find('thunder://')
        if result != -1:    # 字符串存在则 != -1，再次处理
            original_address = original_address.replace('thunder://', '')
            original_address = base64.b64decode(original_address)
            original_address = original_address.decode('gbk')
            original_address = original_address[2:len(original_address) - 2]



    if "flashget://" in original_address:
        original_address = original_address.replace('flashget://', '')
        original_address = original_address.replace('flashget://', '')
        original_address = base64.b64decode(original_address)
        original_address = original_address.decode('gbk')
        original_address = original_address[10:len(original_address) - 10]
    if "qqdl://" in original_address:
        original_address = original_address.replace('qqdl://', '')
        original_address = original_address.replace('qqdl://', '')
        original_address = base64.b64decode(original_address)
        original_address = original_address.decode('gbk')

    ut = url_transform(original_address)

    return {'origin': ut.get('origin'), 'thunder': ut.get('thunder'), 'flashget': ut.get('flashget'), 'qqdl': ut.get('qqdl')}


def url_transform(original_address):
    temp_address = "AA" + original_address + "ZZ"
    temp_address = bytes(temp_address, encoding='gbk')
    thunder_address = "thunder://" + base64.b64encode(temp_address).decode('gbk')

    temp_address = "[FLASHGET]" + original_address + "[FLASHGET]"
    temp_address = bytes(temp_address, encoding='gbk')
    flashget_address = "flashget://" + base64.b64encode(temp_address).decode('gbk')

    temp_address = original_address
    temp_address = bytes(temp_address, encoding='gbk')
    qqdl_address = "qqdl://" + base64.b64encode(temp_address).decode('gbk')

    return {'origin': original_address,'thunder': thunder_address, 'flashget': flashget_address, 'qqdl': qqdl_address }

if __name__ == '__main__':

    address = download_address_translation('thunder://QUF0aHVuZGVyOi8vUVVGbFpESnJPaTh2ZkdacGJHVjhKVVUwSlVKREpVSTRKVVUxSlRnMkpVRTBKVVUwSlVKQkpVSkJMa0pFTVRJNE1DVkZPU1ZCUWlVNU9DVkZOaVZDT0NVNE5TVkZOQ1ZDT0NWQlJDVkZPQ1U0UWlWQ01TVkZOU1U0UmlVNFF5VkZOU1ZCUkNVNU55NXRjRFI4TVRVNU9UUXhNemcyT1h3elJqRTFSVVkxUVVKRU5EWXlPRVZGT1VWRVJUWTFOak5ETWtSQlJVSXpSWHhvUFZGSVZsVklTekpaVEVsRE0wSkRObEZJTjBKQ1QwcFNXVkJCVDFkUFVrVkdmQzlhV2c9PVpa')

    print('原始下载地址:' + (address.get('origin')))
    print('迅雷下载地址:' + address.get('thunder'))
    print('快车下载地址:' + address.get('flashget'))
    print('QQ旋风下载地址:' +  address.get('qqdl'))

