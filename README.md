# Python-API-Train
## 使い方  
### ライブラリのインストール 
`pipenv install`

### docker-composeを用いた起動
```
# まずデータベース起動
docker-compose up -d db
# uwsgiでアプリケーションサーバ起動
docker-compose up -d uwsgi
# Webサーバ起動
docker-compose up -d web
```
### 動作確認 
``` 
curl http://127.0.0.1/ping

curl -X POST -H "Content-Type: application/json" -d '{"user_id":"[user_id]", "password":"[password]"}' http://127.0.0.1/signup

curl -X POST -H "Content-Type: application/json" -d '{"user_id":"[userid]", "password":"[password]"}' http://127.0.0.1/signin
```
