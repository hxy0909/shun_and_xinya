import streamlit as st
import pandas as pd
import datetime

# --- 1. 網頁基本設定 ---
st.set_page_config(page_title="shun & hxy 的戀愛日記", page_icon="☀️")
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
            st.metric("心動指數", f"{days} % ❤️")
        st.success("每一天都值得紀念！")

    st.write("---")
    st.header("⏳ 我們的愛情里程碑")
    with st.expander("2023.05.20 - 第一次告白"):
        st.write("那天雖然下著大雨，但我還是鼓起勇氣說了...")
    with st.expander("2023.12.25 - 一起過的聖誕節"):
        st.write("我們去看了耶誕城，人超級多。")


# === 功能 B: 虛擬寵物 (你原本寫好的邏輯) ===
elif menu == "🐱 虛擬寵物":
    st.subheader("🐱 養一隻屬於我們的寵物")

    # --- 0. 定義寵物圖片資料庫 (你可以換成自己的照片連結) ---
    # 這裡我幫你找了 貓咪、狗狗、水豚 的網路圖片
    PET_ASSETS = {
        "貓咪": {
            "normal": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba", # 普通
            "happy": "https://images.unsplash.com/photo-1533743983669-94fa5c4338ec",  # 開心
            "sad": "https://images.unsplash.com/photo-1573865526739-10659fec78a5",    # 餓/生氣
        },
        "狗狗": {
            "normal": "https://images.unsplash.com/photo-1517849845537-4d257902454a",
            "happy": "https://images.unsplash.com/photo-1587300003388-59208cc962cb",
            "sad": "https://images.unsplash.com/photo-1537151608828-ea2b11777ee8",
        },
        "水豚": {
            "normal": "https://images.unsplash.com/photo-1605092676920-8ac5ae40c7c8",
            "happy": "https://images.unsplash.com/photo-1612531386530-97286d97c2d2",
            "sad": "https://images.unsplash.com/photo-1548681528-6a5c45b66b42",
        }
    }

    # --- 1. 檢查是否已經領養寵物 (狀態初始化) ---
    if 'has_pet' not in st.session_state:
        st.session_state['has_pet'] = False # 預設還沒領養

    # --- 階段 A: 領養介面 (如果還沒領養) ---
    if not st.session_state['has_pet']:
        st.info("👋 歡迎來到寵物中心！請選擇你們想養的動物。")
        
        col1, col2 = st.columns(2)
        with col1:
            # 選擇寵物類型
            pet_type = st.selectbox("想養哪一種？", ["貓咪", "狗狗", "水豚"])
            # 顯示該類型的預覽圖
            st.image(PET_ASSETS[pet_type]["normal"], caption=f"可愛的{pet_type}")
        
        with col2:
            # 輸入名字
            pet_name = st.text_input("幫牠取個名字吧：", placeholder="例如：皮皮")
            
            st.write("---")
            if st.button("💖 確定領養"):
                if pet_name:
                    # 儲存所有寵物資訊
                    st.session_state['has_pet'] = True
                    st.session_state['pet_type'] = pet_type
                    st.session_state['pet_name'] = pet_name
                    st.session_state['pet_hunger'] = 60    # 初始飽食
                    st.session_state['pet_happiness'] = 80 # 初始心情
                    st.rerun() # 重新整理頁面，進入養成模式
                else:
                    st.warning("請先幫牠取個名字喔！")

    # --- 階段 B: 養成介面 (如果已經領養) ---
    else:
        # 取出資料
        name = st.session_state['pet_name']
        p_type = st.session_state['pet_type']
        hunger = st.session_state['pet_hunger']
        happiness = st.session_state['pet_happiness']

        # 顯示標題
        st.markdown(f"### 🏠 {name} 的家 ({p_type})")

        # 決定要顯示哪張圖片 (表情判定邏輯)
        # 1. 如果心情很好 (>80) -> Happy
        # 2. 如果太餓 (<30) 或 心情不好 (<30) -> Sad
        # 3. 其他 -> Normal
        if happiness > 80:
            current_img = PET_ASSETS[p_type]["happy"]
            status_text = f"{name} 看起來超級開心！✨"
        elif hunger < 30 or happiness < 30:
            current_img = PET_ASSETS[p_type]["sad"]
            status_text = f"{name} 覺得有點難過或肚子餓..."
        else:
            current_img = PET_ASSETS[p_type]["normal"]
            status_text = f"{name} 正在發呆。"

        # 介面排版：左邊圖，右邊操作
        img_col, act_col = st.columns([1.5, 1])

        with img_col:
            st.image(current_img, use_container_width=True)
            st.caption(status_text)

        with act_col:
            st.write("📊 **目前狀態**")
            st.write(f"飽食度: {hunger}/100")
            st.progress(hunger)
            st.write(f"心情值: {happiness}/100")
            st.progress(happiness)
            
            st.write("---")
            st.write("✋ **互動**")
            
            if st.button("🍖 餵食 (飽食+10)"):
                st.session_state['pet_hunger'] = min(100, hunger + 10)
                st.session_state['pet_happiness'] = min(100, happiness + 2)
                st.toast(f"{name} 吃了好吃的東西！")
                st.rerun()

            if st.button("🎾 玩耍 (心情+10)"):
                st.session_state['pet_happiness'] = min(100, happiness + 10)
                st.session_state['pet_hunger'] = max(0, hunger - 5) # 玩耍會餓
                st.toast(f"{name} 玩得好瘋！")
                st.rerun()
            
            if st.button("💤 睡覺 (重置心情)"):
                st.session_state['pet_happiness'] = 60
                st.toast(f"{name} 睡了一覺，精神變好了。")
                st.rerun()

        # 重置按鈕 (如果想換寵物)
        st.write("---")
        with st.expander("⚙️ 設定"):
            if st.button("🔄 放生並重新領養 (刪除資料)"):
                st.session_state['has_pet'] = False
                del st.session_state['pet_name']
                st.rerun()

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
# ... (上面是 虛擬寵物、照片牆、悄悄話 的程式碼，請保留不要動) ...

# === 功能 E: 記帳 (保留你剛剛做好的) ===
elif menu == "💰 記帳":
    st.subheader("💰 戀愛公基金 & 分帳計算機")
    if 'bills' not in st.session_state:
        st.session_state['bills'] = pd.DataFrame(columns=["項目", "金額", "誰付的錢", "歸誰的(分帳)"])

    with st.expander("➕ 新增一筆消費", expanded=True):
        c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
        with c1: item_name = st.text_input("項目", placeholder="例如：晚餐")
        with c2: price = st.number_input("金額", min_value=0, step=10)
        with c3: payer = st.selectbox("誰先付的？", ["Shun", "Hxy"])
        with c4: split_method = st.selectbox("算是誰的？", ["平分", "Shun", "Hxy"])

        if st.button("加入清單"):
            new_row = {"項目": item_name, "金額": price, "誰付的錢": payer, "歸誰的(分帳)": split_method}
            st.session_state['bills'] = pd.concat([st.session_state['bills'], pd.DataFrame([new_row])], ignore_index=True)
            st.rerun()

    if not st.session_state['bills'].empty:
        edited_df = st.data_editor(st.session_state['bills'], num_rows="dynamic", use_container_width=True)
        st.session_state['bills'] = edited_df
        
        # 簡易結算顯示
        total = edited_df["金額"].sum()
        st.metric("總花費", f"${total}")


# === 功能 F: 去哪裡玩 (地圖功能) ===
elif menu == "✈️ 去哪裡玩":
    st.subheader("✈️ 我們的旅行足跡 & 願望")
    
    # 1. 建立地圖資料 (經緯度)
    # 這裡預設放幾個台灣著名景點，你可以去 Google Maps 查經緯度換掉
    map_data = pd.DataFrame({
        'lat': [25.0336, 22.9997, 21.9483, 24.1477],
        'lon': [121.5648, 120.2270, 120.7798, 120.6736],
        'name': ['台北101', '台南美食', '墾丁海邊', '台中歌劇院'],
        'type': ['已去過', '想去', '想去', '已去過']
    })

    # 顯示地圖
    st.map(map_data, size=200, color='#ff4b4b') # color 可以改點點顏色
    
    st.write("---")
    st.write("📝 **旅行筆記**")
    st.text_area("想去的清單", "1. 日本環球影城\n2. 迪士尼樂園\n3. 冰島看極光", height=150)


# === 功能 G: 吃什麼東西 (選擇困難救星) ===
elif menu == "🍜 吃什麼東西":
    st.subheader("🍜 今天吃什麼？")
    st.write("不知道吃什麼嗎？交給命運吧！")
    
    # 食物清單
    foods = ["火鍋 🍲", "壽司 🍣", "燒肉 🥩", "義大利麵 🍝", "麥當勞 🍔", "拉麵 🍜", "夜市牛排 🥩", "泰式料理 🌶️", "什麼都不吃 减肥 🥗"]
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # 按鈕特效
        if st.button("🎰 幫我決定！", type="primary"):
            import random
            import time
            
            # 模擬轉盤動畫效果
            placeholder = st.empty()
            for i in range(10):
                placeholder.markdown(f"### 🎲 {random.choice(foods)}")
                time.sleep(0.1)
            
            # 最終結果
            result = random.choice(foods)
            placeholder.markdown(f"### 🎉 命運的選擇：\n# **{result}**")
            st.balloons()

    with col2:
        st.info("💡 如果不喜歡，可以再按一次！")
        # 讓使用者可以自己增加選項
        new_food = st.text_input("想加入新選項？")
        if new_food and st.button("加入"):
            st.toast(f"下次會把 {new_food} 加入轉盤！(目前先用預設的)")


# === 功能 H: 共同願望清單 (進度條) ===
elif menu == "✨ 共同願望清單":
    st.subheader("✨ Together List")
    
    # 這裡示範用 session_state 記住勾選狀態
    # (注意：這只是暫存，重整網頁會重置)
    
    wishes = {
        "一起看一場演唱會": False,
        "一起去日本旅遊": False,
        "學會做一道對方的拿手菜": True, # 預設已完成
        "養一隻寵物": True,
        "擁有一間自己的房子": False
    }
    
    completed_count = 0
    total_count = len(wishes)
    
    st.write("#### 我們的夢想進度")
    
    # 顯示勾選框
    for wish, is_done in wishes.items():
        # 如果勾選，計數+1
        if st.checkbox(wish, value=is_done):
            completed_count += 1
            
    # 計算百分比
    progress = completed_count / total_count
    st.progress(progress)
    st.caption(f"目前完成度：{int(progress * 100)}% ({completed_count}/{total_count})")
    
    if progress == 1.0:
        st.success("太強了！所有願望都達成了！快許下新的願望吧！")


# === 功能 I: 購物清單 (簡易版) ===
elif menu == "🛒 購物清單":
    st.subheader("🛒 購物清單")
    
    # 使用 To-Do List 的寫法
    if 'shopping_list' not in st.session_state:
        st.session_state['shopping_list'] = ["衛生紙", "牛奶", "雞蛋"]
        
    # 新增物品
    col1, col2 = st.columns([3, 1])
    with col1:
        new_item = st.text_input("要買什麼？", label_visibility="collapsed", placeholder="輸入物品名稱...")
    with col2:
        if st.button("➕ 加入") and new_item:
            st.session_state['shopping_list'].append(new_item)
            st.rerun()
            
    # 顯示清單 (可刪除)
    st.write("---")
    for i, item in enumerate(st.session_state['shopping_list']):
        c1, c2 = st.columns([4, 1])
        with c1:
            st.write(f"⬜ {item}")
        with c2:
            if st.button("🗑️", key=f"del_{i}"):
                st.session_state['shopping_list'].pop(i)
                st.rerun()
