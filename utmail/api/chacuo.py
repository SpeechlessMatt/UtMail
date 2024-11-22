import json
import re
from loguru import logger
from ..utmail import Api

class ChacuoOption(Api):
    """
    十分钟邮箱接口
    """
    HEADERS = {
        "Referer": "http://24mail.chacuo.net/",
        "Host": "24mail.chacuo.net",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    }

    def __init__(self):
        Api.__init__(self)
        logger.debug(f"将api源更改为[url]:{self.url}")

    @property
    def url(self):
        return "http://24mail.chacuo.net"

    def get_account(self) -> str|None:
        """获取临时邮箱名称，返回邮箱名称，也可以用 UtMail.account 访问该属性"""
        resp = self.session.get(self.url, headers=self.HEADERS, timeout=5)
        obj = re.compile(r'<input.*?name="converts".*?value="(.*?)"', re.S)
        origin_data = obj.findall(resp.text)[0]
        # 客户端返回json数据中：{...,data:[邮箱]}
        if origin_data == "False":
            return None
        return origin_data + "@chacuo.net"

    def get_inbox(self, details=False) -> list|dict:
        """
        刷新收件箱,返回收件箱
        """
        params = {
            "data": self.account,
            "type": "refresh",
            "arg": ""
        }
        resp = self.session.post(self.url, params=params, headers=self.HEADERS)
        # json 加载
        data = json.loads(resp.text)
        logger.debug(data)
        status = data["status"]
        # 接口处使用列表形式处理
        child_data = data["data"][0]
        email_list = child_data["list"]
        num = child_data["user"]["NUM"]
        if details:
            return {"status": status, "email_list": email_list, "num": num}
        else:
            # 'list': [{'UID': , 'TO': '', 'PATCH': , 'ISREAD': , 'SENDTIME': '', 'FROM': ', 'SUBJECT': '', 'MID': , 'SIZE': 2410}]
            return email_list

    def read_mail(self, MID: str) -> tuple:
        """
        读取邮件信息
        :return: (status: 状态码, email_info: 邮件信息, email_detail: 邮件正文）
        """
        params = {
            "data": self.account,
            "type": "mailinfo",
            "arg": f"f={MID}"
        }
        resp = self.session.post(self.url, params=params, headers=self.HEADERS)
        logger.debug(resp.text)
        # json 加载
        origin_datas = json.loads(resp.text)
        status = origin_datas["status"]
        email_data = origin_datas["data"][0]
        # 邮件简介
        email_info = email_data[0]
        # 邮件正文，包含富文本和普通文本
        email_detail = email_data[1]
        return status, email_info, email_detail

    def delete_mail(self, MID: str) -> bool:
        """
        事实上不需要手动删除邮件，暂时不需要维护这个函数
        """
        try:
            params = {
                "data": self.account,
                "type": "delmail",
                "arg": f"f={MID}"
            }
            resp = self.session.post(self.url, params=params)
            logger.debug(resp.text)
            return True
        except Exception as e:
            logger.warning(e)
            return False


