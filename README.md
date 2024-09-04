<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <!-- バックエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <!-- ミドルウェア一覧 -->
  <img src="https://img.shields.io/badge/-Nginx-269539.svg?logo=nginx&style=for-the-badge">
  <img src="https://img.shields.io/badge/-MySQL-4479A1.svg?logo=mysql&style=for-the-badge&logoColor=white">
  <img src="https://img.shields.io/badge/-Gunicorn-199848.svg?logo=gunicorn&style=for-the-badge&logoColor=white">
  <!-- インフラ一覧 -->
  <img src="https://img.shields.io/badge/-Docker-1488C6.svg?logo=docker&style=for-the-badge">
  <img src="https://img.shields.io/badge/-githubactions-FFFFFF.svg?logo=github-actions&style=for-the-badge">
</p>

## 目次

1. プロジェクトについて
2. 開発環境構築
3. コマンド一覧
4. リモートデバッグの方法
5. トラブルシューティング

<br />
<div align="right">
    <a href="https://pj100.esa.io/posts/4190"><strong>READMEの作成方法 »</strong></a>
</div>
<br />
<div align="right">
    <a href="https://pj100.esa.io/posts/4196"><strong>Dockerfileの詳細 »</strong></a>
</div>
<br />
<!-- プロジェクト名を記載 -->

## プロジェクト名

<!-- プロジェクトについて -->

### プロジェクトについて

<!-- プロジェクトの概要を記載 -->

  <p align="left">
    <br />
    <!-- プロジェクト詳細にBacklogのWikiのリンク -->
    <a href="https://github.com/github_username/repo_name"><strong>プロジェクト詳細 »</strong></a>
    <br />
    <br />

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク等 | バージョン |
| ---------------------- | ---------- |
| Python                 | 3.11.2     |
| Django                 | 4.2.14      |
| Django Rest Framework  | 3.15.0     |
| MySQL                  | 8.0        |

<p align="right">(<a href="#top">トップへ</a>)</p>

## 開発環境構築

<!-- コンテナの作成方法、パッケージのインストール方法など、開発環境構築に必要な情報を記載 -->

### プロジェクトのセットアップ

以下コマンドでプロジェクトで使用するコンテナの作成と起動を行います

```
make prepare
```

### 動作確認

http://127.0.0.1:8000/api/docs にアクセスできたら成功

![スクリーンショット 2023-12-01 9 28 40](https://github.com/pj100-team/template_for_django/assets/41193534/611af768-8fe0-4373-8dc6-42c5dec8e1b2)

### コンテナの停止

以下のコマンドでコンテナを起動します

```
make down
```

## 環境変数

| 変数名                 | 役割                                          | デフォルト値                       | DEV 環境での値                   |
| ---------------------- | --------------------------------------------- | ---------------------------------- | -------------------------------- |
| MYSQL_ROOT_PASSWORD    | MySQL のルートパスワード（Docker で使用）     | root                               |                                  |
| MYSQL_DATABASE         | MySQL のデータベース名（Docker で使用）       | django-db                          |                                  |
| MYSQL_USER             | MySQL のユーザ名（Docker で使用）             | django                             |                                  |
| MYSQL_PASSWORD         | MySQL のパスワード（Docker で使用）           | django                             |                                  |
| MYSQL_HOST             | MySQL のホスト名（Docker で使用）             | db                                 |                                  |
| MYSQL_PORT             | MySQL のポート番号（Docker で使用）           | 3306                               |                                  |
| DJANGO_SECRET_KEY      | Django のシークレットキー                     | secretkey                          | 任意だが、より複雑な値が好ましい |
| DJANGO_ALLOWED_HOSTS   | リクエストを許可するホスト名                  | localhost 127.0.0.1 [::1] back web | フロントのホスト名               |
| DEBUG_FLAG             | デバッグモードの切り替え                      | True                               | False                            |
| TRUSTED_ORIGINS        | CORS で許可するオリジン                       | http://localhost:3000              |                                  |
| DJANGO_SETTINGS_MODULE | Django アプリケーションの設定モジュール       | project.settings.local             | project.settings.dev             |
| CSRF_COOKIE_DOMAIN     | CSRFCookie を設定するときに使用されるドメイン | なし                               | ドメイン名                       |
| SLACK_ENDPOINT_URL     | Slack のエラー通知用 URL                      | なし                               | Slack の Webhook の URL          |

## コマンド一覧

| Make                 | 実行する処理                               | 元のコマンド                                                                               |
| -------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------ |
| make prepare         | イメージのビルドとコンテナの起動を順に行う | docker-compose up -d --build                                                               |
| make up              | コンテナの起動                             | docker-compose up -d                                                                       |
| make build           | イメージのビルド                           | docker-compose build                                                                       |
| make down            | コンテナの停止                             | docker-compose down                                                                        |
| make loaddata        | テストデータの投入                         | docker-compose exec app poetry run python manage.py loaddata crm.json                      |
| make makemigrations  | マイグレーションファイルの作成             | docker-compose exec app poetry run python manage.py makemigrations                         |
| make migrate         | マイグレーションを行う                     | docker-compose exec app poetry run python manage.py migrate                                |
| make show_urls       | エンドポイントをターミナル上で一覧表示     | docker-compose exec app poetry run python manage.py show_urls                              |
| make debugsqlshell   | テストデータの投入                         | docker-compose exec app poetry run python manage.py debugsqlshell                          |
| make createsuperuser | スーパーユーザの作成                       | docker-compose exec app poetry run python manage.py createsuperuser                        |
| make test            | テストを実行                               | docker-compose exec app poetry run pytest                                                  |
| make format          | black と isort を使ってコードを整形        | docker-compose exec app poetry run black . <br> docker-compose exec app poetry run isort . |
| make update          | Poetry 内のパッケージの更新                | docker-compose exec app poetry update                                                      |
| make app             | アプリケーション のコンテナへ入る          | docker exec -it app bash                                                                   |
| make db              | データベースのコンテナへ入る               | docker exec -it db bash                                                                    |

## リモートデバッグの方法

リモートデバッグ を使用する際は以下の url を参考に設定してください<br>
https://pj100.esa.io/posts/4195

## トラブルシューティング

- .env: no such file or directory

.env ファイルがないので作成してください

- docker daemon is not running

Docker Desktop が起動できていないので起動させましょう

- command not found: python

Docker Desktop か docker-compose のバージョンが古すぎるので最新のものにアップデートしましょう

- Ports are not available: address already in use

別のコンテナもしくはローカル上ですでに使っているポートがある可能性があります<br>
下記記事を参考にしてください<br>
https://pj100.esa.io/posts/5023

- Module not found

```
make build
```

を実行して Docker image を更新してください

<p align="right">(<a href="#top">トップへ</a>)</p>
