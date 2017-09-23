import re
import urllib.request
import urllib.parse
import http.cookiejar
import os
from PIL import Image

# 豆瓣登陆的url
login_url = 'https://www.douban.com/accounts/login'
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

params = {
    'form_email': '13547897268',
    'form_password': 'a88888888',
    'source': 'index_nav',
    }

# 从首页提交登陆
response = opener.open(login_url, urllib.parse.urlencode(params).encode('utf-8'))

# 验证成功跳转至登录页
if response.geturl() == 'https://www.douban.com/accounts/login':
    print('跳转至登录页成功')
    html = response.read().decode()

    # 验证码图片地址
    img_url = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if img_url:
        url = img_url.group(1)
        # 将图片保存至同目录下
        res = urllib.request.urlretrieve(url, 'v.JPG')
        
        # 获取captcha-id参数
        captcha = re.search('input type="hidden" name="captcha-id" value="(.+?)"/>', html)
        
        if captcha:
            vcode = input('请输入图片上的验证码：')
            os.remove('v.JPG')
            params['captcha-solution'] = vcode
            params['captcha-id'] = captcha.group(1)
            params['user_login'] = '登陆'
            
            # 提交验证码验证
            response=opener.open(login_url, urllib.parse.urlencode(params).encode('utf-8'))
            
            # 登陆成功，跳转至首页
            if response.geturl() == 'https://www.douban.com/':
                print('login success！')
