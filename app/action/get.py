# encoding:utf-8
# author:wwg
import urllib2,urllib,json
class Get():
    def get(self,post_url,first_post_data):
        """
        发送get请求
        """
        flag = False
        post_url = post_url
        first_post_data = first_post_data
        post_data = urllib.urlencode(first_post_data)
        req = urllib2.Request(post_url, post_data)
        rep = urllib2.urlopen(req)
        result = rep.read()
        dict_result = json.loads(result)

        if dict_result['returnCode'] == 200:
            flag = True
        else:
            flag = flag
        # print flag
        # print dict_result
        return flag, dict_result