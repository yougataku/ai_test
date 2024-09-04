"""ロギングミドルウェア用のモジュール"""
import datetime
import random
from json import JSONDecodeError, loads
from logging import getLogger

from project.constant import LoggerName
from rest_framework import status

application_logger = getLogger(LoggerName.APPLICATION.value)
emergency_logger = getLogger(LoggerName.EMERGENCY.value)


class LoggingMiddleware:
    """APIの開始と終了をロギングするミドルウェア"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.endswith(".js") or request.path in (
            "/api/docs/",
            "/api/schema/",
        ):
            return self.get_response(request)

        ip = get_client_ip(request)
        method = request.method
        path = request.path
        today = datetime.date.today()
        log_id = today.strftime('%Y%m%d') + str(random.randint(1000, 9999))
        # どのユーザの情報をログに載せるかどうかは各プロジェクトに任せます
        # user = request.user

        # if user.is_authenticated:
        #     user_info = f"{user.employee_number}"

        response = self.get_response(request)
        status_code = response.status_code
        message = f"log_id: {log_id} {ip} {method} {path} {status_code}"
        try:
            json = loads(response.content.decode())
            if isinstance(json, dict):
                msg = json.get("msg")
                if msg is not None:
                    message = f"{message}_{msg}"
                detail = json.get("detail")
                if detail is not None:
                    message = f"{message}_{detail}"
        except JSONDecodeError:
            pass
        except AttributeError:
            pass

        if status.is_success(status_code):
            application_logger.info(message)
        else:
            emergency_logger.warning(message)
        return response


def get_client_ip(request):
    """クライアントのIPアドレスを取得"""

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
