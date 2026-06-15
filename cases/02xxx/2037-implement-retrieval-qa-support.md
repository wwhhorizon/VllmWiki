# vllm-project/vllm#2037: Implement Retrieval QA support

| 字段 | 值 |
| --- | --- |
| Issue | [#2037](https://github.com/vllm-project/vllm/issues/2037) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Implement Retrieval QA support

### Issue 正文摘录

I am using a Retriever with a question answer chain and wanted to use vllm for my llm: ` from langchain.llms import VLLM from langchain.chains import RetrievalQA from langchain.vectorstores import FAISS from langchain_core.vectorstores import VectorStoreRetriever vllm = VLLM( model="mosaicml/mpt-7b", trust_remote_code=True, # mandatory for hf models max_new_tokens=128, top_k=10, top_p=0.95, temperature=0.8, ) retriever = VectorStoreRetriever(vectorstore=FAISS(...)) retrievalQA = RetrievalQA.from_llm(llm=vllm,, retriever=retriever) `

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: angchain_core.vectorstores import VectorStoreRetriever vllm = VLLM( model="mosaicml/mpt-7b", trust_remote_code=True, # mandatory for hf models max_new_tokens=128, top_k=10, top_p=0.95, temperature=0.8, ) retriever = Vec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n answer chain and wanted to use vllm for my llm: ` from langchain.llms import VLLM from langchain.chains import RetrievalQA from langchain.vectorstores import FAISS from langchain_core.vectorstores import VectorStoreRe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Implement Retrieval QA support I am using a Retriever with a question answer chain and wanted to use vllm for my llm: ` from langchain.llms import VLLM from langchain.chains import RetrievalQA from langchain.vectorstore...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
