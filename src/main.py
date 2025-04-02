import streamlit as st
from chat_manager import ChatManager

# ページ設定
st.set_page_config(
    page_title="ChatGPT Bot",
    page_icon="🤖",
    layout="wide"
)

# セッション状態の初期化
if "chat_manager" not in st.session_state:
    st.session_state.chat_manager = ChatManager()
if "messages" not in st.session_state:
    st.session_state.messages = []

# タイトル
st.title("ChatGPT Bot 🤖")

# APIキー入力
api_key = st.text_input("OpenAI APIキーを入力してください", type="password")

if api_key:
    try:
        st.session_state.chat_manager.set_api_key(api_key)
    except Exception as e:
        st.error(f"APIキーの設定中にエラーが発生しました: {str(e)}")

# チャット履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ユーザー入力
if prompt := st.chat_input("メッセージを入力してください"):
    if not api_key:
        st.error("APIキーを入力してください")
    else:
        # ユーザーメッセージを表示
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # ChatGPTからの応答を取得
        with st.chat_message("assistant"):
            try:
                response = st.session_state.chat_manager.get_chat_response(prompt)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(str(e))

# クリアボタン
if st.button("チャット履歴をクリア"):
    st.session_state.messages = []
    st.session_state.chat_manager.clear_messages()
    st.rerun() 