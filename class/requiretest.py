import requests


# get
# r = requests.get('https://api.github.com/events')
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'referer':'https://mail.qq.com/',
    'cookie': 'pgv_pvi=8892623872; ptui_loginuin=843004922; pt2gguin=o0843004922; RK=odpkflrEaZ; ptcz=27d2e160cb93fb81e72015dad58b9bd7381b853d35e46d91ff553a15620b5f83; edition=mail.qq.com; webp=1; pgv_pvid=9384442260; ptisp=cnc; uin=o0843004922; skey=@ZbnnfE3wi; p_uin=o0843004922; pt4_token=fihXUTm*3ckqugelAo5oLqA-hpz6b6hfOdXjW23JWjc_; p_skey=uB7oeODdsYdQ3rUOkY5KfDRKhtpgk1tVWCvxOAVju90_; wimrefreshrun=0&; qm_flag=0; qqmail_alias=843004922@qq.com; sid=843004922&bf784874c2a6a8c7fbd9cc7947b646cd,qdUI3b2VPRGRzWWRRM3JVT2tZNUtmRFJLaHRwZ2sxdFZXQ3Z4T0FWanU5MF8.; qm_username=843004922; qm_lg=qm_lg; qm_domain=https://mail.qq.com; qm_ptsk=843004922&@ZbnnfE3wi; foxacc=843004922&0; ssl_edition=sail.qq.com; qm_loginfrom=843004922&wpt; username=843004922&843004922; CCSHOW=000000; new_mail_num=843004922&347'

}
data = {
    'sid': '9A5mqZJK_8TLdkQf',
    'r': 'c0567260a255fc840972583862cc6d06'
}
# post
r = requests.get('https://mail.qq.com/cgi-bin/frame_html', headers=header, params=data)
print(r.text)
