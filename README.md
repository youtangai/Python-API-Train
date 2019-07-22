# Python-API-Train
## 使い方  
### ライブラリの追加  
```  pip install -r requirements.txt ```  
### 起動  
``` python main.py ```  
### 確認とか  
``` curl -X POST -H "Content-Type: application/json" -d '{"userid":"[userid]", "password":"[password]"}' http://127.0.0.1:5000/signup ```  
```  curl -X POST -H "Content-Type: application/json" -d '{"userid":"[userid]", "password":"[password]"}' http://127.0.0.1:5000/signin ```
