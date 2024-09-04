import os
from pydantic_settings import BaseSettings


class VariableSettings(BaseSettings):
    """環境変数を取得する設定クラス"""

    DEBUG_FLAG: bool = os.environ.get("DEBUG_FLAG", True)
    """デバッグモードの切り替え"""
    DJANGO_SECRET_KEY: str = os.environ.get("DJANGO_SECRET_KEY")
    """Djangoのシークレットキー"""
    DJANGO_ALLOWED_HOSTS: str = os.environ.get("DJANGO_ALLOWED_HOSTS")
    """リクエストを許可するホスト名"""
    MYSQL_DATABASE: str = os.environ.get("MYSQL_DATABASE")
    """MYSQLのデータベース名"""
    MYSQL_USER: str = os.environ.get("MYSQL_USER")
    """MYSQLのユーザ名"""
    MYSQL_PASSWORD: str = os.environ.get("MYSQL_PASSWORD")
    """MYSQLのパスワード"""
    MYSQL_HOST: str = os.environ.get("MYSQL_HOST", "db")
    """MYSQLのホスト名"""
    MYSQL_PORT: int = os.environ.get("MYSQL_PORT", 3306)
    """MYSQLのポート番号"""
    DJANGO_SETTINGS_MODULE: str = os.environ.get("DJANGO_SETTINGS_MODULE")
    """Djangoアプリケーションの設定モジュールを指定"""
    TRUSTED_ORIGINS: str = os.environ.get("TRUSTED_ORIGINS")
    """CORSで許可するオリジン"""
    CSRF_COOKIE_DOMAIN: str = os.environ.get("CSRF_COOKIE_DOMAIN", "")
    """CSRFCookieを設定するときに使用されるドメイン"""
    SLACK_ENDPOINT_URL: str = os.environ.get("SLACK_ENDPOINT_URL", "")
    """Slackのエラー通知用URL"""


settings = VariableSettings()
"""Django用の環境変数"""
