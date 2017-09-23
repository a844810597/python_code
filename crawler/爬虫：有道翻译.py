#coding=utf-8
import urllib.request
import urllib.parse
import json
import time
import hashlib


class YouDaoFanYi:
    def __init__(self, api_key, api_keyfrom):
        self.api_key = api_key  # 用户的api_key
        self.api_keyfrom = api_keyfrom  # 用户的api_keyfrom
        self.fromlang = 'auto'  # 翻译前文字语言,auto为自动检查
        self.tolang = 'auto'  # 翻译后文字语言,auto为自动检查
        self.url = 'https://openapi.youdao.com/api/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
            }

    def get_urlencoded_data(self, query):
        '''
        将数据url编码
        :param query: 需要被翻译的文字
        :return: 返回urlencode()编码过的数据
        '''
        salt = str(int(round(time.time() * 1000)))
        sign_str = self.api_key + query + salt + self.api_keyfrom
        sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
        dataform = {
                'q': query,
                'from': self.fromlang,
                'to': self.tolang,
                'appKey' : self.api_key,
                'salt' : salt,
                'sign' : sign
        }
        # 注意是get请求，不是post请求
        data = urllib.parse.urlencode(dataform)
        return data

    def translate(self, query):
        data = self.get_urlencoded_data(query)  # 获取编码的数据
        url = self.url + '?' +data  # 构造目标url
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        self.parse_html(response.read())


    def parse_html(self, html):
        '''
        解析页面，输出翻译结果
        :param html: 翻译返回的页面内容
        :return: None
        '''
        data = json.loads(html)
        print('-' * 50)
        translation_result = data['translation']
        if isinstance(translation_result, list):
            translation_result = translation_result[0]
        print(translation_result)
        if 'basic' in data:
            youdao_result = '\n'.join(data['basic']['explains'])
            print('有道词典结果：')
            print(youdao_result)
        print('-' * 50)


if __name__ == '__main__':
    # 从有道官网申请的API key 和 API keyfrom
    api_key = '4939a3e85bbc63de'
    api_keyfrom = 'kxtBRGbNHuDGB41ifaFZ4Adsw7Qif7fV'
    fanyi = YouDaoFanYi(api_key, api_keyfrom)
    while True:
        query = input('请输入你要翻译的文字[Q | quit 退出]:').strip()
        if query in ['Q', 'quit', 'q']:
            break
        fanyi.translate(query)
        print('\n')
