
"""
接口全局变量
"""
import allure

# 接口全局配置
from Common.Log import MyLog

def dic_to_str(dic):
    s = ''
    for key in dic:
        s+="{0}: {1}\n".format(key,dic[key])
    return s


def logs(func):
    def _func(*args, **kwargs):
        r= func(*args, **kwargs)
        request = "---------------请求-----------------\n{0}\n{1}\n{2}".format(r.url,dic_to_str(r.request.headers),r.request.body)
        MyLog.info(request)
        response = "---------------响应----------------\n{0}\n{1}\n{2}".format(r.status_code,dic_to_str(r.headers),r.text)
        MyLog.info(response)
        allure.attach(request,'请求',allure.attachment_type.TEXT)
        allure.attach(response, '响应', allure.attachment_type.TEXT)
        return r

    return _func