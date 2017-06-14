# encoding:utf-8
# author:
import urllib2,urllib,json
class Post():
    def post(self,post_url,send_data):
        """
        发送post请求
        """
        flag = False
        post_url = post_url
        send_data = send_data
        post_data = urllib.urlencode(send_data)
        req = urllib2.Request(post_url, post_data)
        rep = urllib2.urlopen(req)
        result = rep.read()
        dict_result = json.loads(result)

        if dict_result['returnCode'] == 200:
            flag = True
        else:
            flag = flag
        return flag, dict_result
