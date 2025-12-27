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
elif menu == "💰 記帳":
    st.subheader("💰 戀愛公基金 & 分帳計算機")

    # --- 1. 初始化記帳資料 (暫存於記憶體) ---
    if 'bills' not in st.session_state:
        # 預設建立一個空的 DataFrame 結構
        st.session_state['bills'] = pd.DataFrame(columns=["項目", "金額", "誰付的錢", "歸誰的(分帳)"])

    # --- 2. 新增款項區塊 ---
    with st.expander("➕ 新增一筆消費", expanded=True):
        # 模擬 OCR 功能 (因為沒有 API Key，我們先用模擬按鈕)
        if st.button("📸 [模擬] 掃描收據 (測試用)"):
            # 這裡假裝 AI 讀到了收據內容
            mock_data = pd.DataFrame([
                {"項目": "牛肉麵", "金額": 250, "誰付的錢": "Shun", "歸誰的(分帳)": "平分"},
                {"項目": "珍珠奶茶", "金額": 60, "誰付的錢": "Shun", "歸誰的(分帳)": "Hxy"},
                {"項目": "電影票", "金額": 600, "誰付的錢": "Hxy", "歸誰的(分帳)": "平分"},
            ])
            # 把模擬資料加入目前的帳單
            st.session_state['bills'] = pd.concat([st.session_state['bills'], mock_data], ignore_index=True)
            st.success("AI 成功辨識收據內容！(模擬)")
            st.rerun()

        st.write("--- 或手動輸入 ---")
        c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
        with c1:
            item_name = st.text_input("項目", placeholder="例如：晚餐")
        with c2:
            price = st.number_input("金額", min_value=0, step=10)
        with c3:
            payer = st.selectbox("誰先付的？", ["Shun", "Hxy"])
        with c4:
            # 這裡設定三種邏輯：平分 / 算 Shun 的 / 算 Hxy 的
            split_method = st.selectbox("算是誰的？", ["平分", "Shun", "Hxy"])

        if st.button("加入清單"):
            new_row = {"項目": item_name, "金額": price, "誰付的錢": payer, "歸誰的(分帳)": split_method}
            # 將新資料加入 DataFrame
            st.session_state['bills'] = pd.concat([st.session_state['bills'], pd.DataFrame([new_row])], ignore_index=True)
            st.success(f"已加入：{item_name}")
            st.rerun()

    # --- 3. 互動式表格 (最精華的部分) ---
    if not st.session_state['bills'].empty:
        st.write("### 📝 目前的帳單明細")
        st.info("💡 你可以直接在下方表格修改內容，改完按 Enter 自動更新！")

        # 使用 data_editor 讓表格可以直接編輯！
        edited_df = st.data_editor(
            st.session_state['bills'], 
            num_rows="dynamic", # 允許使用者在表格直接刪除/新增列
            use_container_width=True
        )
        
        # 更新 session_state，確保修改被記住
        st.session_state['bills'] = edited_df

        st.write("---")
        
        # --- 4. 自動結算邏輯 (數學核心) ---
        st.subheader("📊 結算結果")
        
        # 初始化變數
        total_expense = 0
        shun_paid = 0 # Shun 掏出的錢
        hxy_paid = 0  # Hxy 掏出的錢
        shun_should_pay = 0 # Shun 應該負擔的錢
        hxy_should_pay = 0  # Hxy 應該負擔的錢

        # 跑迴圈計算每一筆
        for index, row in edited_df.iterrows():
            cost = row["金額"]
            who_paid = row["誰付的錢"]
            split = row["歸誰的(分帳)"]
            
            total_expense += cost

            # 1. 紀錄誰先墊錢
            if who_paid == "Shun":
                shun_paid += cost
            else:
                hxy_paid += cost
            
            # 2. 計算誰該負責這筆錢
            if split == "平分":
                shun_should_pay += cost / 2
                hxy_should_pay += cost / 2
            elif split == "Shun":
                shun_should_pay += cost
            elif split == "Hxy":
                hxy_should_pay += cost
        
        # 顯示大字報
        c1, c2, c3 = st.columns(3)
        c1.metric("總花費", f"${total_expense}")
        c2.metric("Shun 先墊了", f"${shun_paid}")
        c3.metric("Hxy 先墊了", f"${hxy_paid}")

        st.write("#### 💸 最終結論：")
        
        # 計算差額 (Shun 墊的錢 - Shun 該付的錢)
        # 如果是正的，代表多付了(要收錢)；負的代表少付了(要給錢)
        final_balance = shun_paid - shun_should_pay
        
        if final_balance > 0:
            st.success(f"👉 **Hxy 要給 Shun**： ${abs(final_balance):.0f} 元")
        elif final_balance < 0:
            st.error(f"👉 **Shun 要給 Hxy**： ${abs(final_balance):.0f} 元")
        else:
            st.balloons()
            st.success("🎉 太完美了！兩不相欠！")
            
        # 清除按鈕
        if st.button("🗑️ 全部結清 (清除資料)"):
            st.session_state['bills'] = pd.DataFrame(columns=["項目", "金額", "誰付的錢", "歸誰的(分帳)"])
            st.rerun()

    else:
        st.info("目前還沒有記帳資料，趕快去消費吧！")

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
