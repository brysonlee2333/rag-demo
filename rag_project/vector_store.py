import os

from langchain_chroma import Chroma
import config_data as config
class VectorService(object):
    def __init__(self, embedding):
        self.embedding = embedding
        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=embedding,
            persist_directory=config.persist_directory
        )

    def get_retriever(self):
        """返回向量检索器，方便加入chain"""
        return self.vector_store.as_retriever(search_kwargs={"k":config.similarity_threshold})

if __name__ == "__main__":
    """
    1.利用输入文本转换为向量
    2.在向量库中根据向量查询匹配数据（向量库中的key是向量，根据向量取metadata）
    3.响应数据
    """
    from langchain_community.embeddings import DashScopeEmbeddings
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("DASHSCOPE_API_KEY")
    retriver = VectorService(DashScopeEmbeddings(
        model=config.embedding_model_name,
        dashscope_api_key=api_key
    )).get_retriever()
    res = retriver.invoke("我的体重180斤，尺码推荐")
    print(res)