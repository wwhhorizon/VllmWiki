# vllm-project/vllm#33986: [Tracking issue]: Issue Tracker for Qwen/Qwen3-VL-Embedding & Qwen/Qwen3-VL-Reranker

| 字段 | 值 |
| --- | --- |
| Issue | [#33986](https://github.com/vllm-project/vllm/issues/33986) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking issue]: Issue Tracker for Qwen/Qwen3-VL-Embedding & Qwen/Qwen3-VL-Reranker

### Issue 正文摘录

### vLLM examples for Qwen3-VL-Embedding : - https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/vision_embedding_offline.py - https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/vision_embedding_online.py ### vLLM examples for Qwen3-VL-Reranker: - https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_rerank_api_online.py - https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_score_api_online.py - https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_reranker_offline.py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Tracking issue]: Issue Tracker for Qwen/Qwen3-VL-Embedding & Qwen/Qwen3-VL-Reranker usage ### vLLM examples for Qwen3-VL-Embedding : - https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/vision_embedd...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
