#pip install python-dotenv
#Streamlit 패키지 추가
#streamlit run 06_voicebot_ui_main_api_key.py
import streamlit as st


#OpenAI 패키지 추가
import openai
import os
from dotenv import load_dotenv

#.env 파일 경로 지정
load_dotenv()

# audiorecorder 패키지 추가 :  Streamlit 애플리케이션에서 오디오를 녹음할 수 있는 컴포넌트를 제공
# pip install streamlit-audiorecorder

from audiorecorder import audiorecorder

##시간 정보를 위한 패키지 추가
from datetime import datetime

#Open AI API 키 설정하기
api_key = os.environ.get("OPEN_API_KEY")

client = openai.OpenAI(api_key=api_key)

### 기능 구현 함수 ###
def STT(speech):
    #파일 저장
    filename='input.mp3'
    speech.export(filename,format="mp3")
    
    #음원 파일 열기
    with open(filename, "rb") as audio_file:
        #Whisper model 활용해 text 얻기
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    #파일 삭제
    os.remove(filename)

    return transcription.text


### 메인 함수 ###

def main():
    #기본 설정
    st.set_page_config(
        page_title="Sound Chatbot Program",
        layout="wide")
    
    #제목
    st.header("Sound Chatbot Program")

    #구분선
    st.markdown("---")

    #기본 설명
    with st.expander("About S.Chatbot Program", expanded=True):
        st.write(
        """
        - We use Streamlit for UI of S.Chatbot Pro\n
        - We use Whisper of OpenAI for STT/n
        - Answers will provided by OpenAI's GPT Model.\n
        - We use OpenAI's TTS service
        """
        )

        st.markdown("---")

    system_content = "You are a thoughtful assistant. Respond to all input in 25 words and anser in English."

    #session state 초기화
    if "chat" not in st.session_state:
        st.session_state["chat"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role":"system","content":system_content}]

    if "check_reset" not in st.session_state:
        st.session_state["check_reset"] = [False]

    #사이드바 생성
    with st.sidebar:

        #GPT 모델을 선택하기 위한 라디오 버튼
        model = st.radio(label="GPT model", options=["gpt-3.5-turbo","gpt-4o","gpt-4-turbo"])

        st.markdown("---")

        #make reset button
        if st.button(label="reset"):
            #reset code
            pass

    #기능 구현 공간
    col1, col2 = st.columns(2)
    with col1:
        #왼쪽 영역 작성
        st.subheader("Ask Question")

        # 음성 녹음 아이콘 추가
        audio = audiorecorder()

        if (audio.duration_seconds > 0 ) and (st.session_state["Check_reset"]==False):
            #음성 재생
            st.audio(audio.export().read())
            

    with col2:
        #오른쪽 영역 작성
        st.subheader("Question & Answer")

if __name__=="__main__":
    main()