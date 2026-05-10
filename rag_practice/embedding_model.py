import os
import time
from dotenv import load_dotenv
from langchain_classic.embeddings import CacheBackedEmbeddings
from langchain_classic.storage import LocalFileStore
from langchain_community.embeddings import DashScopeEmbeddings

# 使用DashScopeEmbeddings需要提前导包 uv add dashscope
# 1.加载环境变量
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

# 2.新建嵌入式向量模型
underlying_embeddings = DashScopeEmbeddings(
    model="text-embedding-v1",
    dashscope_api_key=api_key
)
# 3.配置缓存，设置缓存可显著提升嵌入式向量计算速度，也可节省token
# This isn't for production use, but is useful for local
# query_embedding_cache=True 使用缓存，这个参数需要设置，默认为False
store = LocalFileStore("./cache/")
cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings,
    store,
    namespace=underlying_embeddings.model,
    query_embedding_cache=True
)
# Example: caching a query embedding
tic  = time.time()
print(cached_embedder.embed_query("Hello, my name is jack!"))
print(f"First call took: {time.time() - tic:.2f} seconds")

# subsequent calls use the cache
tic = time.time()
print(cached_embedder.embed_query("Hello, my name is jack!"))
print(f"Second call took: {time.time() - tic:.2f} seconds")