# 临时邮箱 TMail
<p align="center">
    <a href="https://github.com/SpeechlessMatt/UtMail" target="_blank" style="margin-right: 20px; font-style: normal; text-decoration: none;">
        <img src="https://img.shields.io/github/stars/SpeechlessMatt/UtMail" alt="Github Stars" />
    </a>
    <a href="https://github.com/SpeechlessMatt/UtMail" target="_blank" style="margin-right: 20px; font-style: normal; text-decoration: none;">
        <img src="https://img.shields.io/github/stars/SpeechlessMatt/UtMail" alt="Github Forks" />
    </a>
    <a href="https://github.com/SpeechlessMatt/UtMail" target="_blank" style="margin-right: 20px; font-style: normal; text-decoration: none;">
        <img src="https://img.shields.io/github/languages/code-size/SpeechlessMatt/UtMail" alt="Code-size" />
    </a>
    <a href="https://github.com/SpeechlessMatt/UtMail" target="_blank" style="margin-right: 20px; font-style: normal; text-decoration: none;">
        <img src="https://img.shields.io/github/v/release/SpeechlessMatt/UtMail?display_name=tag&sort=semver" alt="version" />
    </a>
</p>

本项目旨在收集临时邮箱的接口，并提供统一的方法调用

- 欢迎使用本项目

- 欢迎开发者为本项目接入新的接口 

## 使用方法

### 下载并导入库
Git方式

```git clone --depth=1 https://github.com/SpeechlessMatt/UtMail.git```

pip方式

```pip install utmail```
### 引用方法
`from utmail import UtMail`

对于临时收件箱，该库主要有以下方法：
- **get_account()**: 连接邮箱服务器，申请临时邮箱地址
- **get_inbox(details)**: 获取收件箱，返回一个列表/字典
    - arg: 
        - （可选）details=**bool** False则返回一个列表，仅包含列表，否则返回包含status_code,num的字典

- **read_mail(MID)**: 读取邮件，返回元组
    - arg:
        - MID=**(str)** 从get_inbox()返回值中获得MID，通过MID读取邮件详细信息
    - return:
        - **tuple**(状态码，邮件简介，邮件正文)

- **delete_mail(MID)**: 删除邮件，返回布鲁值
    - arg:
        - MID=**(str)** 参考read_mail()
    - return:
        - **bool** 删除是否成功

> **注意：**
> 本库使用[**loguru**](https://github.com/Delgan/loguru)日志处理库，可以在主程序头部增加如下代码以关闭日志输出
```python
import sys
from loguru import logger
logger.remove()
# 日志级别详情参考loguru库 这里最低级别为INFO
logger.add(sys.stderr, level="warning") 
```

### 简单实例

```python
from utmail import UtMail, ChacuoOption
import time

if __name__ == '__main__':
    # 创建实例对象 调用api接口ChacuoOption()
    tm = UtMail(ChacuoOption())
    # 申请邮箱
    name = tm.get_account()
    while True:
        # 获取收件箱
        email_list = tm.get_inbox()
        # 输出列表
        print(email_list)
        if len(email_list) != 0:
            a = input("MID:")
            # 读取邮箱
            print(tm.read_mail(a))
        for i in range(0, 10):
            print(f"\r{10 - i}秒后自动刷新...", end="", flush=True)
            time.sleep(1)
        print("\r\n")
```
## 目前支持的API接口
- **ChacuoOption()**: [十分钟邮箱](http://24mail.chacuo.net/)

## 项目维护者
[@Czy_4201b](https://github.com/SpeechlessMatt)

## 开发者文档
- 暂无文档

