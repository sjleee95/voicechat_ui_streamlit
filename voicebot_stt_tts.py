import streamlit as st

def main():

    st.set_page_config(page_title="음성 챗봇 프로그램", layout="wide")

    #우
    st.header("음성 챗봇 프로그램")

    #구분선
    st.markdown("---")
    with st.expander(
        "음성 챗봇에 관하여", expanded=True):
        st.write(
        """"
        - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
        - STT는 OPENAI의 Whisper을 사용합니다.
        - 답변은 OPENAI의 GPT 모델을 활용합니다.
        - TTS는 OpenAI의 TTS를 활용합니다.
        """
        )

        #비어있는 칸 추가
        st.markdown("")

if __name__=="__main__":
    main()