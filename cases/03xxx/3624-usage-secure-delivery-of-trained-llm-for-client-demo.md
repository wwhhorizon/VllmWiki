# vllm-project/vllm#3624: [Usage] Secure Delivery of Trained LLM for Client Demo

| 字段 | 值 |
| --- | --- |
| Issue | [#3624](https://github.com/vllm-project/vllm/issues/3624) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage] Secure Delivery of Trained LLM for Client Demo

### Issue 正文摘录

I have recently trained a LLM based on llama-2 using a private dataset for a client. They require the model for a demo on their machines. Unfortunately, I don't have the option to host the model and provide them with an endpoint. The model size is approximately 68GB, and it's stored in SafeTensors. Additionally, I have developed a binary for inference+RAG pipeline. I am using vLLM for inference. The model is located within a folder . The client needs to test the demo on their local machines. I am seeking advice on the best possible secure method to deliver the LLM model to the client while ensuring that the model files are encrypted to prevent misuse. Given the sensitivity of the model and its potential misuse, encryption is crucial to maintain data security.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Trained LLM for Client Demo usage I have recently trained a LLM based on llama-2 using a private dataset for a client. They require the model for a demo on their machines. Unfortunately, I don't have the option to host...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the sensitivity of the model and its potential misuse, encryption is crucial to maintain data security.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: or inference. The model is located within a folder . The client needs to test the demo on their local machines. I am seeking advice on the best possible secure method to deliver the LLM model to the client while ensurin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
