---
layout: default
title: 如何开发api文件？
nav_order: 1
---

# 如何开发一个api文件？
开发api用的语言是python，你需要创建一个example.py 其中，example是你为api取的名字 推荐使用命名规则

## 📚 api文档介绍
- 本项目调用了requests库中的requests.session()方法，并在UtMail()内定义了self.session()并将其隐式传入Api()类中

所以，example.py文件中至少包含如下内容：
```python
# 从utmail中引用Api类
from utmail import Api

# 继承Api类的方法和属性
class Example(Api):
    # 获取父类的属性 包含了上文提到的session()
    def __init__(self):
        Api.__init__(self)
```

通过继承父类的方式，你可以通过父类中__init__()中self.session()拿到session,所以你可以直接调用：
```python
self.session.get(url, headers=headers)
self.session.post(url, headers=headers)
...
```
参考ChacuoOption:(仅展示关心部分)

```python
import ...

class ChacuoOption(Api):
    def __init__(self):
        Api.__init__(self)
    ...
    # 获取邮箱账户的方法名字必须是get_account()
    def get_account(self) -> str|None:
        # 调用requests.session的get方法
        resp = self.session.get(self.url, headers=self.HEADERS, timeout=5)
```
除了提供session之外，Api还提供了self.account和self.token属性，当然你可以选择不使用他们，但是建议:session最好不要另开一个requests.session而是如上文那样直接使用Api的session

这样会更加方便管理同时减少连接数量，优化代码结构，而且保证cookies不会轻易丢失

- self.account :邮箱账户名字，完整的(如example@qq.com)
- self.token :部分网站需要先申请token

直接使用父类的account和token有助于用户通过UtMail.account或UtMail.token访问属性

## 📚 重载方法目录

就如ChacuoOption中一样，ChacuoOption重载了UtMail类中的方法:
- get_account(): 获取邮箱账户，需要返回`str`，即账户名字，建议在返回账户名字之前也为self.account赋值，如上文所说，有助于用户通过UtMail.account访问属性

- get_inbox(details=False): 获取收件箱列表，返回`list`，注意：details=False形参要填，即使用不上，否则会报错

- read_mail(MID): 形参MID传入邮件ID（这个ID可以自己指定，但是要保证邮件列表中可以看到邮件ID）返回一个`tuple`，可以包含服务器的状态码，也可以只返回邮件信息，当然建议返回的元组应为：(状态码，邮件简介，邮件正文)

- delete_mail(MID): MID如上解释，返回`bool`，即删除是否成功

如果不重载以上方法，用户调用时会引发异常：

**ApiFuncUndefined：所使用的Api接口未定义该方法**

如果：
```python
def get_inbox(self):
    pass
```
则不会引起异常，但是得不到任何结果

# 模板文件.py
```python
from ..utmail import Api

class ChacuoOption(Api):
    def __init__(self):
        Api.__init__(self)

    def get_account(self) -> str|None:
        ...
        # 经过一系列方法获得account
        # 记得给父类self.account赋值
        self.account = account
        return self.account

    def get_inbox(self, details=False) -> list|dict:
        ...
        # 经过一系列方法获得inbox_list
        return inbox_list

    def read_mail(self, MID: str) -> tuple:
        ...
        # 经过一系列方法
        return mail

    def delete_mail(self, MID: str) -> bool:
        ...
        # 经过一系列方法
        return is_success
```
具体方法也可以参考本项目 [utmail/api/chacuo.py](https://github.com/SpeechlessMatt/UtMail/blob/main/utmail/api/chacuo.py)

# 开发者联系方式
- github上的issue

