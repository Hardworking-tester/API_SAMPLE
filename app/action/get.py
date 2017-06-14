# encoding:utf-8
# author:wwg
import urllib2,urllib,json
class Get():
    def get(self,post_url):
        """
        发送get请求
        """

        url = post_url
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        print res
