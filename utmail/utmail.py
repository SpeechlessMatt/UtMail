import requests
from loguru import logger

class Api:
    def __init__(self):
        # session来源于requests.session(),需要UtMail()进行初始化
        # 开发Api请查看Api文档
        self.session = None
        # 所获取的的邮箱账户
        self.account = None
        # 可能需要的token
        self.token = None

    def get_account(self) -> str | None:
        """
        获取临时邮箱名称，返回邮箱名称，也可以用 UtMail.account 访问该属性
        :return: 临时邮箱名称
        """
        raise ApiFuncUndefined("所使用的Api接口未定义该方法：<get_account>")

    def get_inbox(self, details=False) -> list | dict:
        """
        刷新收件箱,返回收件箱
        :param
        details: 是否详细输出，包含服务器信息
        :return:
        list 返回邮件列表
        dict 返回详细字典(details=True)
        """
        raise ApiFuncUndefined("所使用的Api接口未定义该方法：<get_inbox>")

    def read_mail(self, MID: str) -> tuple:
        """
        读取邮件信息
        :param MID: 邮件ID -可以通过get_email_list()方法拿到
        :return: (status: 状态码, email_info: 邮件信息, email_detail: 邮件正文）
        """
        raise ApiFuncUndefined("所使用的Api接口未定义该方法：<read_mail>")

    def delete_mail(self, MID: str) -> bool:
        """
        事实上不需要手动删除邮件，暂时不需要维护这个函数
        :param MID: 邮件ID
        :return: bool 成功与否
        """
        raise ApiFuncUndefined("所使用的Api接口未定义该方法：<delete_account>")

class UtMail:
    """
    UtMail: 嵌入式的python，你可以根据开发者文档为该项目适配更多的api接口，本项目的目的式创造一个统一的接口
    感谢您为本项目贡献，感谢您使用本项目
    """
    def __init__(self, option: Api) -> None:
        self._url = ""
        self.session = requests.session()
        self.account = None
        self.option = option
        # 隐式传入必要参数session：requests.session避免出现不必要的多连接，方便统一管理
        option.session = self.session

    def __del__(self) -> None:
        logger.trace("调用删除函数")
        self.session.close()

    def close(self):
        self.__del__()

    def get_account(self) -> str | None:
        """
        获取临时邮箱名称，返回邮箱名称，也可以用 UtMail.account 访问该属性
        :return: 临时邮箱名称
        """
        return self.option.get_account()

    def get_inbox(self, details=False) -> list | dict:
        """
        刷新收件箱,返回收件箱
        :param details: 是否详细输出，包含服务器信息
        :return: list 返回邮件列表
        dict 返回详细字典(details=True)
        """
        return self.option.get_inbox(details)

    def read_mail(self, MID: str) -> tuple:
        """
        读取邮件信息
        :param MID: 邮件ID -可以通过get_email_list()方法拿到
        :return: (status: 状态码, email_info: 邮件信息, email_detail: 邮件正文）
        """
        return self.option.read_mail(MID)

    def delete_mail(self, MID: str) -> bool:
        """
        事实上不需要手动删除邮件，暂时不需要维护这个函数
        :param MID: 邮件ID
        :return: bool 成功与否
        """
        return self.option.delete_mail(MID)


class ApiFuncUndefined(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
