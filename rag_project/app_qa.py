import streamlit as st
import config_data as config
from rag import RagService

st.title("智能客服")
st.divider() #分隔符

# 使用session_state存储消息记录和rag服务对象
if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content": "你好，有什么可以帮你？"}]

if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 在页面最下方提供用户输入栏
prompt = st.chat_input()

if prompt:
    # 在页面输出用户的提问,并存储用户消息
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    ai_res_list = []
    with st.spinner("AI思考中。。。"):
        res = st.session_state["rag"].chain.invoke({"input": prompt}, config.session_config)
        st.chat_message("assistant").write(res)
        st.session_state["message"].append({"role": "assistant", "content": res})


