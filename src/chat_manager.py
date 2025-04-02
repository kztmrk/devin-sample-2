import openai
from typing import List, Dict, Optional

class ChatManager:
    def __init__(self):
        self.client = None
        self.messages: List[Dict[str, str]] = []

    def set_api_key(self, api_key: str) -> None:
        """APIキーを設定します"""
        openai.api_key = api_key
        self.client = openai.OpenAI()

    def add_message(self, role: str, content: str) -> None:
        """メッセージを追加します"""
        self.messages.append({"role": role, "content": content})

    def get_chat_response(self, user_message: str) -> Optional[str]:
        """ChatGPTからの応答を取得します"""
        if not self.client:
            raise ValueError("APIキーが設定されていません")

        try:
            # ユーザーメッセージを追加
            self.add_message("user", user_message)

            # ChatGPTからの応答を取得
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.messages
            )

            # アシスタントの応答を取得
            assistant_message = response.choices[0].message.content

            # アシスタントの応答を履歴に追加
            self.add_message("assistant", assistant_message)

            return assistant_message

        except Exception as e:
            raise Exception(f"ChatGPT APIとの通信中にエラーが発生しました: {str(e)}")

    def clear_messages(self) -> None:
        """メッセージ履歴をクリアします"""
        self.messages = [] 