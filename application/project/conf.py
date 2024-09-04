"""設定ファイル用のモジュール"""

import tomllib
from typing import Any, Optional


class ConfFile:
    """confファイル取得用クラス
    Attributes:
        _conf_data (Optional[dict[Any, Any]]): pyproject.tomlのデータを辞書形式に変換した内容<br>
            最初の1回だけ読み込まれる
    """

    _conf_data: Optional[dict[Any, Any]] = None

    @classmethod
    def get(cls) -> dict[Any, Any]:
        """pyproject.tomlのデータを辞書形式で返す
        2回目以降はファイルの読み込みは実施しない
        Returns:
            dict[Any, Any]: pyproject.tomlの設定データの辞書形式
        """
        if cls._conf_data is None:
            with open("pyproject.toml", mode="rb") as file:
                cls._conf_data = tomllib.load(file)
        return cls._conf_data
