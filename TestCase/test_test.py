import pytest
import allure
from Common import Assert
from Common import Request
import json

assertions = Assert.Assertions()
request = Request.Request()
token = ''


# @allure.severity("critical")  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.feature("功能模块")  # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
class TestShoppingTrolley(object):

    @allure.story("登录")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    # @allure.issue("BUG号：123")  # 问题表识，关联标识已有的问题，可为一个url链接地址
    # @allure.testcase("测试登录")  # 用例标识，关联标识用例，可为一个url链接地址
    def test_case_example(self):
        data = {"password": "1234561", "username": "admin"}
        post_request = request.post_request("http://qa.guoyasoft.com:8099/admin/login", json=data)
        assertions.assert_code(post_request.status_code, 200)
        respJson = post_request.json()
        respData = respJson['data']
        token = respData['token']
        tokenHead = respData['tokenHead']
        token = tokenHead + ' ' + token

    @allure.story("其他")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    def test_case(self):
        data = {"password": "123456", "username": "admin"}
        post_request = request.post_request("http://qa.guoyasoft.com:8099/admin/login", json=data)
        assertions.assert_code(post_request.status_code, 200)

        print(token)

    @allure.story("文件")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    def test_upload(self):
        files = {'file': open('/test.png', 'rb'), 'customerId': 5}
        response = request.post_request_multipart('http://www.bg.guoyasoft.com/api/upload/stu/addPic', files=files)
        print(response.text)
        pass
