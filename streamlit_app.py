import streamlit as st
import time

# 앱 제목
st.title("🎮 30초 Click 게임")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "game_active" not in st.session_state:
    st.session_state.game_active = False

# 게임 시작 함수
def start_game():
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.game_active = True

# 버튼 클릭 시 점수 증가
def add_score():
    if st.session_state.game_active:
        st.session_state.score += 1

# "게임 시작" 버튼
if st.button("게임 시작"):
    start_game()

# 남은 시간 계산
if st.session_state.game_active:
    elapsed = time.time() - st.session_state.start_time
    remaining = 30 - int(elapsed)
    if remaining > 0:
        st.write(f"⏳ 남은 시간: {remaining}초")
        st.button("Click!", on_click=add_score)
        st.write(f"현재 점수: {st.session_state.score}")
    else:
        st.session_state.game_active = False
        st.write("✅ 게임 종료!")
        st.success(f"총 클릭 수: {st.session_state.score}")

# 처음 접속 시 안내
if not st.session_state.game_active and st.session_state.start_time is None:
    st.info("👉 '게임 시작' 버튼을 눌러주세요.")
