"""定数関連のモジュール
"""
from enum import Enum


class LoggerName(Enum):
    """ロガー名"""

    APPLICATION = "application"
    """アプリケーションロガー用"""
    EMERGENCY = "emergency"
    """エマージェンシーロガー用"""
