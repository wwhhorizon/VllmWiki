# vllm-project/vllm#20899: [Bug]: Fix MRL Support Detection for Qwen3-Embedding-8B Model (It Supports MRL per Latest Official Docs)

| 字段 | 值 |
| --- | --- |
| Issue | [#20899](https://github.com/vllm-project/vllm/issues/20899) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fix MRL Support Detection for Qwen3-Embedding-8B Model (It Supports MRL per Latest Official Docs)

### Issue 正文摘录

### Your current environment Unfortunately, I cannot run the Python script to collect the environment due to certain security considerations and restrictions within the organization.But I can briefly describe the key environmental information. ### 🐛 Describe the bug ### Environment - vLLM Version: 0.8.5 - Hardware: Unknown - Python Version: Unknown (Torch 2.6.0) - Model: Qwen3-Embedding-8B ### Description I'm using the Qwen3-Embedding-8B model deployed via vLLM in a platform (Cherry Studio). When making embedding calls with the "dimensions" parameter included in the request (e.g., {"model": "Qwen3-Embedding-8B", "input": "hi", "dimensions": 1024}), vLLM returns a 400 Bad Request error stating that the model does not support Matryoshka Representation Learning (MRL). However, according to the latest official technical documentation from Alibaba (released in June 2025), Qwen3-Embedding-8B explicitly supports MRL, allowing dynamic dimension adjustment without quality loss. This indicates a bug in vLLM's model detection logic, where it incorrectly assumes the model lacks MRL support. This is problematic because: - In my case, the platform (Cherry Studio) automatically includes "dimensi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Fix MRL Support Detection for Qwen3-Embedding-8B Model (It Supports MRL per Latest Official Docs) bug ### Your current environment Unfortunately, I cannot run the Python script to collect the environment due to c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t Detection for Qwen3-Embedding-8B Model (It Supports MRL per Latest Official Docs) bug ### Your current environment Unfortunately, I cannot run the Python script to collect the environment due to certain security consi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n making embedding calls with the "dimensions" parameter included in the request (e.g., {"model": "Qwen3-Embedding-8B", "input": "hi", "dimensions": 1024}), vLLM returns a 400 Bad Request error stating that the model do...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ase, the platform (Cherry Studio) automatically includes "dimensions" in backend requests for optimization, leading to failures in knowledge base embedding and search functionalities. - The platform developers confirmed...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: K), but actual workflows fail due to the forced parameter. ### Steps to Reproduce 1. Deploy Qwen3-Embedding-8B using vLLM 0.8.5. 2. Send a POST request to the embeddings endpoint with "dimensions" included, e.g.: { "mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
