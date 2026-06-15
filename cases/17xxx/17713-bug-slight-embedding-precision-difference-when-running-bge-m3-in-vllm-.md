# vllm-project/vllm#17713: [Bug]: Slight Embedding Precision Difference When Running bge-m3 in vLLM Compared to Original Model

| 字段 | 值 |
| --- | --- |
| Issue | [#17713](https://github.com/vllm-project/vllm/issues/17713) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Slight Embedding Precision Difference When Running bge-m3 in vLLM Compared to Original Model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying the BAAI/bge-m3 embedding model using vLLM, I observed that the generated embedding vectors exhibit small but consistent differences compared to those produced by the same model running in HuggingFace Transformers or ONNXRuntime. ﻿ The difference is typically around 1e-5 to 1e-4 per dimension. ``` from FlagEmbedding import BGEM3FlagModel model = BGEM3FlagModel('BAAI/bge-m3') sentences_1 = ["What is BGE M3?"] embeddings_1 = model.encode(sentences_1,batch_size=12, max_length=8192,) dense_vecs = embeddings_1["dense_vecs"] print(dense_vecs) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Slight Embedding Precision Difference When Running bge-m3 in vLLM Compared to Original Model bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the BAAI/bge-m3 embedding model using vLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: odel using vLLM, I observed that the generated embedding vectors exhibit small but consistent differences compared to those produced by the same model running in HuggingFace Transformers or ONNXRuntime. ﻿ The difference...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng Precision Difference When Running bge-m3 in vLLM Compared to Original Model bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the BAAI/bge-m3 embedding model using vLLM, I observed that the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Slight Embedding Precision Difference When Running bge-m3 in vLLM Compared to Original Model bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the BAAI/bge-m3 embedding model using vLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on Difference When Running bge-m3 in vLLM Compared to Original Model bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the BAAI/bge-m3 embedding model using vLLM, I observed that the generated...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
