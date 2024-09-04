import json
from logging import getLogger

import requests
from django.utils.log import AdminEmailHandler

from project.constant import LoggerName
from project.environment_variables import settings


class SlackHandler(AdminEmailHandler):
    def send_mail(self, subject, message, *args, **kwargs):
        webhook_url = settings.SLACK_ENDPOINT_URL
        if "Request" in message:
            alarm_emoji = ":rotating_light:"
            error_msg = message.split("META")[0]
            text = alarm_emoji + error_msg
            data = json.dumps(
                {
                    "attachments": [{"color": "#e01d5a", "text": text}],
                }
            )
            headers = {"Content-Type": "application/json"}
            getLogger(LoggerName.EMERGENCY.value).error(error_msg)
            requests.post(url=webhook_url, data=data, headers=headers)
