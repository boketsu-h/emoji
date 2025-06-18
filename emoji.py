import streamlit as st

def add_emoji(text):
    # キーワードに応じて絵文字を追加する例（最低限）
    emoji_map = {
        "楽しい": "😄",
        "疲れた": "😩",
        "美味しい": "😋",
        "眠い": "😴",
        "最高": "✨",
        "友達": "👯",
        "勉強": "📚",
        "怒": "😡",
        "笑": "😂",
        "泣": "😭"
    }

    for word, emoji in emoji_map.items():
        text = text.replace(word, word + emoji)
    return text

# StreamlitのUI部分
st.title("絵文字ジェネレーター")
user_input = st.text_area("文章を入力してね：")
if st.button("絵文字つける！") and user_input:
    result = add_emoji(user_input)
    st.markdown("### ✨ 結果")
    st.write(result)
