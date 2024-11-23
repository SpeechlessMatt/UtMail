---
layout: default
title: 🚀 快速开始
nav_order: 1
---

# 🚀 制作一个简易自动收件箱
让我们开始做一个简单的程序吧~😀

<blockquote>
    <p dir="auto">
如果你还没有安装本库，详情看 <a href="./index.md/#-如何简单地下载">这里</a>
    </p>
</blockquote>

## 📕 步骤

### 1. 导入utmail

下载完成后，使用 `import` 导入包：

```python
from utmail import UtMail
```
或者

```python
import utmail
```
### 2. 导入你喜欢的api接口
- 例如：ChacuoOption

```python
import ChacuoOption
```

### 3. 开始愉快地使用吧！

```python
from utmail import UtMail

tm = UtMail(ChacuoOption())
# 申请一个随机邮箱 返回这个邮箱的名字
name = tm.get_account()
# 获取收件箱 返回一个含有MID的列表
email_list = tm.get_inbox()
# 读取邮件 例如MID为2102456 返回(邮件简介，邮件正文)
email = tm.read_mail("2102456")
# 删除文件
tm.delete_mail("21002456")
```

<blockquote>
    <p dir="auto">
<strong>⚠ 警告：</strong>调用get_account(),read_mail()等方法的时候会使用requests向服务器发送请求，<font color=red>切勿频繁发送请求，对接口造成破坏</font>
    </p>
</blockquote>

<a href="index.md/#-免责声明">免责声明</a>

**正确示例:**
```python
while True:
  # 建议至少10s查取一次邮箱
  time.sleep(10)
  tm.get_inbox()
```
