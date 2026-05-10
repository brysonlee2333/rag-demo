import os
from langchain_community.document_loaders import BiliBiliLoader
from dotenv import load_dotenv

load_dotenv()
loader = BiliBiliLoader(
    ["https://www.bilibili.com/video/BV1XkDrBaEXm/"],
    # SESSDATA、bili_jct、buvid3这三个值需要在登陆状态下从cookie中查找，定期会变化
    sessdata=os.getenv("SESSDATA"),
    bili_jct=os.getenv("BILI_JCT"),
    buvid3=os.getenv("BUVID3"),
)

docs = loader.load()

# 输出结果
print(f"加载到 {len(docs)} 个文档\n")
print("=== 第一个文档内容 ===")
print(docs[0].page_content[:1000] + "...")  # 打印前500字符