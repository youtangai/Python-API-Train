# Python-API-Train
## 使い方  
### ライブラリのインストール 
`pip install -r requirements.txt`
### 起動  
```
# 通常起動
python main.py
# debug起動
FLASK_DEBUG=1 python main.py
```
### docker-composeを用いた起動
```
# まずデータベース起動
docker-compose up -d db
# apiサーバを起動
docker-compose up -d api
```
### 動作確認 
``` 
curl http://localhost:5000/ping

curl -X POST -H "Content-Type: application/json" -d '{"user_id":"[user_id]", "password":"[password]"}' http://127.0.0.1:5000/signup

curl -X POST -H "Content-Type: application/json" -d '{"user_id":"[userid]", "password":"[password]"}' http://127.0.0.1:5000/signin
```
