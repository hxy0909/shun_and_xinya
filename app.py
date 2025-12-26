import streamlit as st
import pandas as pd
import datetime

# 1. 設定網頁標題
st.set_page_config(page_title="shun & hxy", page_icon="❤️")
st.title("🧑🏻‍❤️‍👩🏻 我們的戀愛日記")
st.audio("bgm.ogg", format="audio/mp3") 
# 如果你暫時沒有 mp3 檔，可以用下面這行測試 (Streamlit 範例音樂)：
#st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg")
# 2. 左側選單
menu = st.sidebar.selectbox(
    "使用模式", 
    ["虛擬寵物", "記帳", "照片牆", "悄悄話", "去哪裡玩","吃什麼東西","共同願望清單","購物清單"]
)

# 3. 不同的頁面內容


if menu == "虛擬寵物":
    st.subheader("🐱 養一隻屬於我們的貓")

    # --- 1. 設定寵物的記憶 (如果沒有就建立) ---
    if 'pet_hunger' not in st.session_state:
        st.session_state['pet_hunger'] = 50  # 飽食度 (0-100)
    if 'pet_happiness' not in st.session_state:
        st.session_state['pet_happiness'] = 50 # 心情 (0-100)

    # --- 2. 定義互動功能 (按鈕邏輯) ---
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🍖 餵食"):
            # 吃飯：飽食+10，心情+5
            st.session_state['pet_hunger'] = min(100, st.session_state['pet_hunger'] + 10)
            st.session_state['pet_happiness'] = min(100, st.session_state['pet_happiness'] + 5)
            st.toast("好吃！飽食度上升了！") # 顯示右下角小提示

    with col2:
        if st.button("🎾 玩耍"):
            # 玩耍：心情+10，但會餓 (飽食-5)
            st.session_state['pet_happiness'] = min(100, st.session_state['pet_happiness'] + 10)
            st.session_state['pet_hunger'] = max(0, st.session_state['pet_hunger'] - 5)
            st.toast("好開心！心情變好了！")

    with col3:
        if st.button("💤 睡覺"):
            # 睡覺：雖然無聊但能恢復體力 (範例)
            st.session_state['pet_happiness'] = 50 # 重置心情
            st.toast("貓咪睡著了...噓！")

    st.write("---")

    # --- 3. 顯示寵物狀態與表情 ---
    # 使用 columns 把 圖片 放左邊，數據 放右邊
    p_col1, p_col2 = st.columns([1, 2])

    with p_col1:
        # 根據心情決定顯示哪張圖 (這裡用超大 Emoji 代替圖片，你也可以換成 st.image)
        happiness = st.session_state['pet_happiness']
        hunger = st.session_state['pet_hunger']

        if hunger < 20:
            st.markdown("# 😵") # 餓昏了
            pet_status = "我快餓扁了..."
        elif happiness > 80:
            st.markdown("# 😸") # 超開心
            pet_status = "喵～今天心情超棒！"
        elif happiness < 30:
            st.markdown("# 😾") # 生氣
            pet_status = "哼！不理你了！"
        else:
            st.markdown("# 🐱") # 普通
            pet_status = "發呆中..."
        
        st.caption(pet_status)

    with p_col2:
        st.write("📊 **寵物狀態**")
        
        # 飽食度條
        st.write(f"飽食度: {st.session_state['pet_hunger']}/100")
        st.progress(st.session_state['pet_hunger'])
        
        # 心情條
        st.write(f"心情值: {st.session_state['pet_happiness']}/100")
        st.progress(st.session_state['pet_happiness'])

elif menu == "愛的照片":
    st.subheader("📸 我們的照片牆")
    # 這裡先用網路圖片代替，確保你能成功執行
    col1, col2 = st.columns(2)
    with col1:
        st.image("photos/love1.jpg", caption="我們的第一張合照")
    with col2:
        st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba", caption="可愛的貓貓")

elif menu == "悄悄話":
    st.subheader("💌 寫信給我")
    msg = st.text_area("想說什麼？")
    if st.button("發送"):
        st.snow() # 氣球特效

        st.write(f"收到你的訊息了：{msg}")

elif menu == "計時器":
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
