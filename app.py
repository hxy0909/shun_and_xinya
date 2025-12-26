import streamlit as st
import pandas as pd
import datetime

# 1. 設定網頁標題
st.set_page_config(page_title="我們的回憶", page_icon="❤️")
st.title("🧑🏻‍❤️‍👩🏻 我們的戀愛日記")
st.audio("bgm.ogg", format="audio/mp3") 
# 如果你暫時沒有 mp3 檔，可以用下面這行測試 (Streamlit 範例音樂)：
#st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg")
# 2. 左側選單
menu = st.sidebar.radio("瀏覽模式", ["計時器", "愛的照片", "悄悄話"])

# 3. 不同的頁面內容
if menu == "計時器":
    st.subheader("我們先來算算日子...")
    # --- 請修改這裡的日期 (年, 月, 日) ---
    start_date = datetime.date(2025, 9, 17) 
    today = datetime.date.today()
    days = (today - start_date).days
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("我們已經在一起", f"{days} 天")
    with col2:
        st.metric("心動指數", f"{days}% ")
        
    st.success("每一天都值得紀念！")
    st.write("---") # 分隔線
    st.header("⏳ 我們的愛情里程碑")

    # 第一個里程碑
    with st.expander("2023.05.20 - 第一次告白"):
        st.write("那天雖然下著大雨，但我還是鼓起勇氣說了...")
        st.write("你驚訝的表情我現在還記得！")
        # 如果有那天的照片，也可以放這裡
        # st.image("img/day1.jpg") 

    # 第二個里程碑
    with st.expander("2023.12.25 - 一起過的聖誕節"):
        st.write("我們去看了耶誕城，人超級多，但牽著你的手就不覺得擠。")
        st.write("晚餐吃了很好吃的義大利麵 🍝")

    # 第三個里程碑
    with st.expander("2024.02.14 - 情人節驚喜"):
        st.write("沒想到你會送我親手做的卡片！")
        st.write("這是我收過最棒的禮物。")

elif menu == "愛的照片":
    st.subheader("📸 我們的照片牆")
    # 這裡先用網路圖片代替，確保你能成功執行
    col1, col2 = st.columns(2)
    with col1:
        st.image("photos/love1.jpg", caption="這是我們第一張合照")
    with col2:
        st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba", caption="可愛的貓貓")

elif menu == "悄悄話":
    st.subheader("💌 寫信給我")
    msg = st.text_area("想說什麼？")
    if st.button("發送"):
        st.snow() # 氣球特效

        st.write(f"收到你的訊息了：{msg}")
