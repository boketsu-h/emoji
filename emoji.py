import streamlit as st

def add_emoji(text):
    emoji_map = {
        "楽しい": "😄",
        "疲れた": "😩",
        "美味しい": "😋",
        "眠い": "😴",
        "嬉しい": "(^○^)",
        "最高": "✨",
        "友達": "👯",
        "勉強": "📚",
        "怒": "😡",
        "笑": "😂",
        "泣": "😭"
    }

    for word, emoji in emoji_map.items():
        if word in text:
            text = text.replace(word, word + emoji)
    return text

st.title("絵文字ジェネレーター")
user_input = st.text_area("文章を入力してね：")

if st.button("絵文字つける！") and user_input:
    result = add_emoji(user_input)
    st.markdown("### ✨ 結果")
    st.code(result, language="")  # 見やすい表示＋コピーしやすい

    # コピー用ボタン（HTML + JS）
    st.markdown(f"""
        <button onclick="navigator.clipboard.writeText(`{result}`)">📋 コピーする</button>
    """, unsafe_allow_html=True)
