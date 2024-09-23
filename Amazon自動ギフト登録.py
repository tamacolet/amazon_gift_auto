from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chromeのオプションを設定
chrome_options = Options()

# ユーザーデータディレクトリを指定
# Windowsの場合の例：
user_data_dir = r"C:\Users\"ユーザー名\AppData\Local\Google\Chrome\User Data"
# Macの場合の例：
# user_data_dir = r"/Users/YourUsername/Library/Application Support/Google/Chrome"

chrome_options.add_argument(f"user-data-dir={user_data_dir}")

# 特定のプロファイルを使用する場合（オプション）
chrome_options.add_argument("profile-directory=Default")

# ギフトカードコードのリスト

gift_card_codes = [
    "コード1",
    "コード2",
    "コード3",
    # 必要な数だけコードを追加してください
    #chatgptで生成すると簡単です
]

# WebDriverの初期化
driver = webdriver.Chrome(options=chrome_options)

# Amazonのギフトカード登録ページにアクセス
driver.get("https://www.amazon.co.jp/gc/redeem")

# 各ギフトカードコードに対して処理を繰り返す
for code in gift_card_codes:
    try:
        # 入力フィールドが表示されるまで待機
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "gc-redemption-input"))
        )
        
        # コードを入力
        input_field.clear()
        input_field.send_keys(code)
        
        # 登録ボタンをクリック
        submit_button = driver.find_element(By.ID, "gc-redemption-apply-button")
        submit_button.click()
        
        # 処理完了まで少し待機
        time.sleep(5)
        
        # ページを再読み込み
        driver.refresh()
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        continue

# ブラウザを閉じる
driver.quit()
