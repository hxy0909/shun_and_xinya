import streamlit as st
import pandas as pd
import datetime

# --- 1. 網頁基本設定 ---
st.set_page_config(page_title="shun & hxy 的戀愛日記", page_icon="❤️")
st.title("🧑🏻‍❤️‍👩🏻 我們的戀愛日記")

# 背景音樂 (請確認你的資料夾內有 bgm.ogg 或 bgm.mp3)
# st.audio("bgm.ogg", format="audio/ogg") 

# --- 2. 左側選單 (這裡定義了所有功能) ---
menu = st.sidebar.selectbox(
    "使用模式", 
    [
        "🏠 戀愛計時器", 
        "🐱 虛擬寵物", 
        "📸 照片牆", 
        "💌 悄悄話", 
        "💰 記帳", 
        "✈️ 去哪裡玩",
        "🍜 吃什麼東西",
        "✨ 共同願望清單",
        "🛒 購物清單"
    ]
)

# --- 3. 不同的頁面內容 ---

# === 功能 A: 戀愛計時器 (原本的計時器功能) ===
if menu == "🏠 戀愛計時器":
    st.subheader("我們在一起的日子...")
    
    # --- 請修改這裡的日期 (年, 月, 日) ---
    start_date = datetime.date(2025, 9, 17) 
    today = datetime.date.today()
    days = (today - start_date).days
    
    # 防止日期還沒到出現負數 (如果是未來日期)
    if days < 0:
        st.info(f"距離我們的紀念日還有 {abs(days)} 天！")
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("我們已經在一起", f"{days} 天")
        with col2:
            st.metric("心動指數", f"100% ❤️")
        st.success("每一天都值得紀念！")

    st.write("---")
    st.header("⏳ 我們的愛情里程碑")
    with st.expander("2023.05.20 - 第一次告白"):
        st.write("那天雖然下著大雨，但我還是鼓起勇氣說了...")
    with st.expander("2023.12.25 - 一起過的聖誕節"):
        st.write("我們去看了耶誕城，人超級多。")


# === 功能 B: 虛擬寵物 (你原本寫好的邏輯) ===
elif menu == "🐱 虛擬寵物":
    st.subheader("🐱 養一隻屬於我們的貓")

    # 1. 設定寵物狀態
    if 'pet_hunger' not in st.session_state:
        st.session_state['pet_hunger'] = 50
    if 'pet_happiness' not in st.session_state:
        st.session_state['pet_happiness'] = 50

    # 2. 互動按鈕
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🍖 餵食"):
            st.session_state['pet_hunger'] = min(100, st.session_state['pet_hunger'] + 10)
            st.session_state['pet_happiness'] = min(100, st.session_state['pet_happiness'] + 5)
            st.toast("好吃！飽食度上升了！")
    with col2:
        if st.button("🎾 玩耍"):
            st.session_state['pet_happiness'] = min(100, st.session_state['pet_happiness'] + 10)
            st.session_state['pet_hunger'] = max(0, st.session_state['pet_hunger'] - 5)
            st.toast("好開心！心情變好了！")
    with col3:
        if st.button("💤 睡覺"):
            st.session_state['pet_happiness'] = 50 
            st.toast("貓咪睡著了...噓！")

    st.write("---")

    # 3. 顯示狀態與表情
    p_col1, p_col2 = st.columns([1, 2])
    with p_col1:
        happiness = st.session_state['pet_happiness']
        hunger = st.session_state['pet_hunger']
        
        if hunger < 20:
            st.markdown("# 😵")
            st.caption("我快餓扁了...")
        elif happiness > 80:
            st.markdown("# 😸")
            st.caption("喵～今天心情超棒！")
        elif happiness < 30:
            st.markdown("# 😾")
            st.caption("哼！不理你了！")
        else:
            st.markdown("# 🐱")
            st.caption("發呆中...")

    with p_col2:
        st.write("📊 **寵物狀態**")
        st.write(f"飽食度: {hunger}/100")
        st.progress(hunger)
        st.write(f"心情值: {happiness}/100")
        st.progress(happiness)


# === 功能 C: 照片牆 ===
elif menu == "📸 照片牆":
    st.subheader("📸 我們的照片牆")
    col1, col2 = st.columns(2)
    with col1:
        # 注意：請確認資料夾名稱是 photos 還是 img，以及副檔名
        # st.image("photos/love1.jpg", caption="我們的第一張合照")
        st.write("(這裡放照片1)")
    with col2:
        st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba", caption="可愛的貓貓")


# === 功能 D: 悄悄話 ===
elif menu == "💌 悄悄話":
    st.subheader("💌 寫信給我")
    msg = st.text_area("想說什麼？")
    if st.button("發送"):
        st.snow()
        st.write(f"收到你的訊息了：{msg}")


# === 其他未完成的功能 (先放個佔位符) ===
elif menu == "💰 記帳":
    st.subheader("💰 戀愛公基金")
    st.info("🚧 這個功能正在施工中... 敬請期待！")

elif menu == "✈️ 去哪裡玩":
    st.subheader("✈️ 旅行計畫")
    st.info("🚧 趕快來規劃下次去哪裡玩吧！")

elif menu == "🍜 吃什麼東西":
    st.subheader("🍜 今天吃什麼？")
    if st.button("幫我決定！"):
        import random
        foods = ["火鍋", "義大利麵", "燒肉", "壽司", "麥當勞", "牛肉麵"]
        st.success(f"今天就吃：{random.choice(foods)}！")

elif menu == "✨ 共同願望清單":
    st.subheader("✨ Together List")
    st.checkbox("一起看極光")
    st.checkbox("一起養一隻狗")
    st.checkbox("學會做蛋糕")

elif menu == "🛒 購物清單":
    st.subheader("🛒 要買的東西")
    st.text_input("輸入要買的物品...")
