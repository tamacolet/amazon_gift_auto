# amazon_gift_auto
予めまとめて入力したアマゾンギフト券を、自動で1つずつAmazonアカウントに登録します。

メインのChromeブラウザで動くので、ログインの必要がありません。

Pythonスクリプトで動きます。


## 準備
### 13行目
    user_data_dir = r"C:\Users\"ユーザー名\AppData\Local\Google\Chrome\User Data"

ユーザー名を自分のPCのユーザー名に書き換えてください。


### 24行目

アマゾンギフト券のコードを入力してください。

    gift_card_codes = [

    "コード1",
    
    "コード2",
    
    "コード3",
    
    # 必要な数だけコードを追加してください
    
    #chatgptで生成すると簡単です
    
    ]


※自己責任でご使用ください。
