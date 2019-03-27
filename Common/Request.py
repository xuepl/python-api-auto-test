
"""
封装request
"""

import os
import random
import requests
from Common import Log
from Common.Consts import *


class Request:

    def __init__(self):
        """
        :param env:
        """
        self.log = Log.MyLog()
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}




    def get(self,url,params,headers,cookies=None):
        if(headers):
            headers = dict(self.headers,**headers)
        return requests.get(url, params=params, headers=headers,cookies=cookies)

    def post(self,url,data=None,params=None,headers=None,files=None,json=None,cookies=None):
        if (headers):
            headers = dict(self.headers, **headers)
        return requests.post(url,data=data,params=params,headers=headers,files=files,json=json,cookies=cookies)

    @logs
    def get_request(self,url,params=None,headers=None,cookies=None):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:
        """

        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:

            response = requests.get(url, params, headers=headers, cookies = cookies)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        self.log.info('----请求用时: %s 秒数' % time_consuming)

        return response

    @logs
    def post_request(self,url,data=None,params=None,headers=None,json=None,cookies=None):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            response = requests.post(url,data=data,params=params,headers=headers,json=json, cookies=cookies)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        self.log.info('----请求用时: %s 秒数' % time_consuming)

        return response

    @logs
    def post_request_multipart(self, url,files=None, headers=None, cookies=None):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        response = requests.post(url=url, files=files, headers=headers,cookies=cookies)
        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        self.log.info('----请求用时: %s 秒数' %time_consuming)

        return response

    @logs
    def put_request(self, url, data, header,cookies=None):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header, cookies=cookies)
            else:
                response = requests.put(url=url, params=data, headers=header, cookies=cookies)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        self.log.info('----请求用时: %s 秒数' % time_consuming)

        return response