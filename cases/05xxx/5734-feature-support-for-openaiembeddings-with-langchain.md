# vllm-project/vllm#5734: [Feature]: Support for OpenAIEmbeddings with Langchain

| 字段 | 值 |
| --- | --- |
| Issue | [#5734](https://github.com/vllm-project/vllm/issues/5734) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for OpenAIEmbeddings with Langchain

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have hosted `e5-mistral-7b-instruct` with vllm OpenAI compatible APIs and it can be accessed by Posting to `http://localhost:8000/v1/embeddings` with: ``` { "model": "e5-mistral-7b-instruct", "input":["A sentence to encode."] } ``` However, it seems **cannot be accessed through Langchain** with: ``` from langchain_openai import OpenAIEmbeddings emb_model = OpenAIEmbeddings( model="e5-mistral-7b-instruct", openai_api_base="http://localhost:8000/v1", openai_api_key="EMPTY") emb_model.embed_query("A sentence to encode.") ``` **Error received:** ``` openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'base64 encoding is not currently supported', 'type': 'BadRequestError', 'param': None, 'code': 400} ``` Will it be supported in Langchain? Or have I done anything wrong? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: **cannot be accessed through Langchain** with: ``` from langchain_openai import OpenAIEmbeddings emb_model = OpenAIEmbeddings( model="e5-mistral-7b-instruct", openai_api_base="http://localhost:8000/v1", openai_api_key="...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sed by Posting to `http://localhost:8000/v1/embeddings` with: ``` { "model": "e5-mistral-7b-instruct", "input":["A sentence to encode."] } ``` However, it seems **cannot be accessed through Langchain** with: ``` from la...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Support for OpenAIEmbeddings with Langchain good first issue;feature request ### 🚀 The feature, motivation and pitch I have hosted `e5-mistral-7b-instruct` with vllm OpenAI compatible APIs and it can be accessed by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
