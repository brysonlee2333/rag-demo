"""
text splitters break large docs into smaller chunks that will be retrievable individually and fit
within model context window limit
"""
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

with open("./data/test1.txt") as f:
    text1 = f.read()

# 块间目标重叠长度。重叠chunk能够缓解上下文被分割时造成的信息丢失问题。重叠让边界上下文同时存在于前后两个块中，向量检索会自然向后检索。
text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    length_function=len,
    is_separator_regex=False
)

texts = text_spliter.split_text(text1)
for text in texts:
    print("="*20)
    print(text)

markdown_document = "# Foo\n\n    ## Bar\n\nHi this is Jim\n\nHi this is Joe\n\n ### Boo \n\n Hi this is Lance \n\n ## Baz\n\n Hi this is Molly"

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_document)
for md in md_header_splits:
    print(md)
