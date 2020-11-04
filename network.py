import requests
from requests import Timeout, ConnectionError, HTTPError, TooManyRedirects, URLRequired, RequestException
from bs4 import BeautifulSoup
from config import config


class Network:
    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
        }
        self.uniformUrl = 'https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D1'
        self.nonUniformUrl = 'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&'

    def check(self):
        try:
            respone = requests.get('http://www.baidu.com', timeout=10)
            return True
        except Timeout as e:
            print('connect baidu timeout.')
        except ConnectionError as e:
            print('connect baidu error.')
        except HTTPError as e:
            print('HTTPError')
        except TooManyRedirects as e:
            print('TooManyRedirects')
        except URLRequired as e:
            print('URLRequired')
        except RequestException as e:
            print('RequestException')
        except requests.exceptions.RequestException as e:
            print('anyway, it is a request error')
        except BaseException as e:
            print('wtf?')
        return False

    def unifiedLogin(self):
        sess = requests.session()
        response = sess.get(self.uniformUrl, headers=self.header)

        soup = BeautifulSoup(response.text, 'html.parser')
        lt = soup.find('input', id='lt')['value']

        dataBody = {
            'un': config['username'],
            'pd': config['password'],
            'lt': lt,
            'ul': len(config['username']),
            'pl': len(config['password']),
            'rsa': config['username'] + config['password'] + lt,
            'execution': 'e1s1',
            '_eventId': 'submit'
        }
        try:
            sess.post(self.uniformUrl, headers=self.header, data=dataBody)
        # except Timeout as e:
        #     print('post timeout.')
        # except ConnectionError as e:
        #     print('post connect error.')
        # except HTTPError as e:
        #     print('post HTTPError')
        # except TooManyRedirects as e:
        #     print('post TooManyRedirects')
        # except URLRequired as e:
        #     print('post URLRequired')
        # except RequestException as e:
        #     print('post RequestException')
        except requests.exceptions.RequestException as e:
            print(e)
            print('post error :(')
        except BaseException as e:
            print('wtf?')
        

    def NonUnifiedLogin(self):
        sess = requests.session()
        response = sess.get(self.nonUniformUrl, headers=self.header)

        dataBody = {
            'username': config['username'],
            'password': config['password'],
            'action': 'login',
            'ac_id': '1',
            'user_ip': '',
            'nas_ip': '',
            'user_mac': '',
            'url': '',
            'save_me': '0'
        }
        try:
            sess.post(self.nonUniformUrl, headers=self.header, data=dataBody)
        except requests.exceptions.RequestException as e:
            print(e)
            print('post error :(')
        except BaseException as e:
            print('wtf?')
