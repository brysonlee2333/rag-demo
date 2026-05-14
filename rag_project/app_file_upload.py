import streamlit as st
import time
from knowledge_base import KnowledgeBaseService

# cd命令切换到文件所在目录，执行命令 streamlit run 文件名, 网页访问地址http://localhost:8501
# 当web页面元素发生变化时，则代码重新执行一遍
# 添加标题
st.title("知识库更新服务")

# file upload
upload_file = st.file_uploader(
    label="请上传TXT文件",
    type=["txt"],
    accept_multiple_files=False
)

if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if upload_file is not None:
    file_name = upload_file.name
    file_type = upload_file.type
    file_size = upload_file.size/1024 #kb

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式：{file_type}|大小：{file_size:.2f}KB")
    text = upload_file.getvalue().decode("utf-8")
    with st.spinner("载入知识库中。。。"):
        time.sleep(1)  # 模拟执行延迟，让加载提示展示
        result = st.session_state["service"].upload_by_str(text, file_name)
        st.write(result)