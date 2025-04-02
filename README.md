# Streamlit ChatGPT Bot

シンプルなStreamlitベースのChatGPTチャットボット

## 機能

- ChatGPT APIを使用したチャット機能
- APIキーの動的入力
- シンプルなチャットインターフェース

## 必要条件

- Python 3.8以上
- OpenAI APIキー

## セットアップ

1. 依存パッケージのインストール:
```bash
pip install -r requirements.txt
```

2. アプリケーションの起動:
```bash
streamlit run src/main.py
```

## 使用方法

1. アプリケーションを起動すると、ブラウザで自動的に開きます
2. APIキーを入力フィールドに入力します
3. チャットメッセージを入力して送信します
4. ChatGPTからの応答が表示されます

## 注意事項

- APIキーはセッション中のみ保持されます
- チャット履歴は保存されません 