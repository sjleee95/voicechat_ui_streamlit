import streamlit as st

##메인 함수 ##
def main():

#기본 설정
    st.set_page_config(
        page_title='음성 챗봅 프로그램',
        layout='wide'
    )

    #제목
    st.header("음성 챗봇 프로그램")

    #구분선
    st.markdown("---")

    #기본 설명
    with st.expander("음성 챗봇 프로그램에 관하여", expanded=True):
        st.write(
        """
        - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
        - STT(Speech-To-Text)는 OpenAI의 Whisper를 활용합니다. 
        - 답변은 OpenAI의 GPT 모델을 활용합니다. 
        - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
        """
        )

        st.markdown("")


        #사이드바 생성
    with st.sidebar:

        #GPT 모델 선택 위한 라디오 버튼
        model = st.radio(label='GPT 모델', options = ["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo"])
        st.markdown("---")

        #리셋 버튼 생성
        if st.button(label="초기화"):
            #리셋 코드
            pass

if __name__=="__main__":
    main()