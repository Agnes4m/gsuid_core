import fastapi_amis_admin

from gsuid_core.version import __version__ as gscore_version

web_url = 'https://docs.sayu-bot.com'
login_html = f'''
<html>
<head>
<style>
  div {{
    background: rgba(255, 255, 255, 0.6) url('/webstatic/bg.jpg');
    background-blend-mode: screen;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
  }}
</style>
</head>
<p>
  <p align='center'>
      <a href='{web_url}'>
          <img src='/webstatic/ICON.png'
          width='256' height='256' alt='GenshinUID'>
      </a>
  </p>
  <h1 align='center'>GsCore 网页控制台</h1>
  <div align='center'>
      <a href='{web_url}/Started/InstallCore.html' target='_blank'>
      安装文档</a> &nbsp; · &nbsp;
      <a href='{web_url}/PluginsHelp/GenshinUID.html/'
      target='_blank'>指令列表</a> &nbsp; · &nbsp;
      <a href='{web_url}/FAQ/'>常见问题</a>
  </div>
  <h5 align='center'>
    ✨支持连接HoshinoBot · NoneBot2 · Koishi · Yunzai · ZeroBot的多功能Bot插件核心✨
  </h5>
  <h5 align='center'>
    ✨支持平台: QQ群/频道 · Onebot v11/v12 · WeChat · 飞书 · Tg · Kook/dodo · Dc · 米游社✨
  </h5>
</p>
</html>
'''

footer_html = f'''
<p align='right'>
    <div class='p-2 text-center bg-light'>Copyright © 2021 - 2024
        <a href='https://github.com/KimigaiiWuyi/GenshinUID' target='_blank'
         class='link-secondary'>GenshinUID {gscore_version}
        </a>
         X
        <a target='_blank'
         href='https://github.com/amisadmin/fastapi_amis_admin/'
         class='link-secondary' rel='noopener'>
         fastapi_amis_admin {fastapi_amis_admin.__version__}
        </a>
    </div>
</p>
'''

gsuid_webconsole_help = '''
## 初次使用

欢迎进入网页控制台!

Admin账户可以通过左侧的选项进入不同的数据库直接修改,**首次登陆的Admin账户别忘了修改你的密码!**

普通账户可以通过左侧的选项进行绑定CK或者SK

未来还会加入更多功能!

## 丨我该如何获取Cookies？[#92](https://github.com/KimigaiiWuyi/GenshinUID/issues/92)
（[@RemKeeper](https://github.com/RemKeeper)）

```js
var cookie = document.cookie;
var Str_Num = cookie.indexOf('_MHYUUID=');
cookie = cookie.substring(Str_Num);
var ask = confirm('Cookie:' + cookie + '按确认，然后粘贴至Cookies或者Login_ticket选框内');
if (ask == true) {
  copy(cookie);
  msg = cookie
} else {
  msg = 'Cancel'
}
```

1. 复制上面全部代码，然后打开[米游社BBS](https://bbs.mihoyo.com/ys/)
2. 在页面上右键检查或者Ctrl+Shift+i
3. 选择控制台（Console），粘贴，回车，在弹出的窗口点确认（点完自动复制）
4. 然后在和机器人的私聊窗口，粘贴发送即可

**警告：Cookies属于个人隐私，其效用相当于账号密码，请勿随意公开！**

## 丨获取米游社Stoken([AutoMihoyoBBS](https://github.com/Womsxd/AutoMihoyoBBS))

```js
var cookie = document.cookie;
var ask = confirm('Cookie:' + cookie + '按确认，然后粘贴至Cookies或者Login_ticket选框内');
if (ask == true) {
  copy(cookie);
  msg = cookie
} else {
  msg = 'Cancel'
}
```

1. 复制上面全部代码，然后打开[米游社账户登录界面](http://user.mihoyo.com/)
2. 在页面上右键检查或者Ctrl+Shift+i
3. 选择控制台（Console），粘贴，回车，在弹出的窗口点确认（点完自动复制）
4. 然后在和机器人的私聊窗口，粘贴发送即可

**警告：Cookies属于个人隐私，其效用相当于账号密码，请勿随意公开！**

## 获取CK通则

**如果获取到的Cookies字段不全，无法通过校验**
**推荐重新登陆米游社再进行获取**

## 网页端 #92 [@RemKeeper](https://github.com/RemKeeper)
[通过网页控制台简易获取Cookies](https://github.com/KimigaiiWuyi/GenshinUID/issues/92)
## 安卓 [@shirokurakana](https://github.com/shirokurakana)
[通过额外APP获取Cookies](https://github.com/KimigaiiWuyi/GenshinUID/issues/203)
## IOS [@741807012](https://github.com/741807012)
[通过快捷指令获取Cookies](https://github.com/KimigaiiWuyi/GenshinUID/issues/201)
'''
