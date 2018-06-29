import requests
import json, time


class qqMusic(object):

    def __init__(self):
        self.date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    def get_json(self):
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'referer': 'https://y.qq.com/n/yqq/toplist/4.html',
        }
        params = {
            'tpl': '3',
            'page': 'detail',
            'date': '2018-05-29',
            'topid': '4',
            'type': 'top',
            'song_begin': '0',
            'song_num': '30',
            'g_tk': '5381',
            'jsonpCallback': 'MusicJsonCallbacktoplist',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'jsonp',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq',
            'needNewCode': '0',
        }
        url = 'http://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg'
        r = requests.get(url, headers=header, params=params).text
        init_data = r.replace('MusicJsonCallbacktoplist(', '').rstrip(')')
        """
        到这知识获取到歌曲相关信息 但没有歌曲的链接
        接下来取出songmid， 获取歌曲链接
        """
        json_data = json.loads(init_data)
        return json_data

    def get_link(self, songmid):
        url = 'http://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg'
        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'referer':'https://y.qq.com/portal/player.html'
        }
        """
        songmid,filename是变量
        """
        params = {
            'g_tk': '5381',
            'jsonpCallback': 'MusicJsonCallback2584168335259782',
            'loginUin': 0,
            'hostUin': 0,
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': 0,
            'platform': 'yqq',
            'needNewCode': 0,
            'cid': '205361747',
            'callback': 'MusicJsonCallback2584168335259782',
            'uin': 0,
            'songmid': songmid,
            'filename': 'C400'+songmid+'.m4a',
            'guid': '9384442260'
        }
        r = requests.get(url, headers=header, params=params).text
        init_data = r.split('(')[1].rstrip(')')
        data = json.loads(init_data)

        data = data['data']['items'][0]
        url = 'http://dl.stream.qqmusic.qq.com/'+data['filename']+'?vkey='+data['vkey']+'&guid=9384442260&uin=0&fromtag=66'
        print(url)


q = qqMusic()
paihang = q.get_json()
for i in paihang['songlist']:
    q.get_link(i['data']['songmid'])
