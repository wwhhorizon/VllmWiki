# vllm-project/vllm#42911: [Bug]: vllm0.19.1 with llmcache with qwen3.6-27B-FP8 failed

| 字段 | 值 |
| --- | --- |
| Issue | [#42911](https://github.com/vllm-project/vllm/issues/42911) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm0.19.1 with llmcache with qwen3.6-27B-FP8 failed

### Issue 正文摘录

### Your current environment ubuntu22.04 vllm/vllm-openai:v0.19.1 ### 🐛 Describe the bug [Bug]: vllm0.19.1 with llmcache with qwen3.6-27B-FP8 failed (EngineCore pid=120) ERROR 05-18 01:31:14 [core.py:1108] ValueError: Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type. but if i add --no-disable-hybrid-kv-cache-manager it says:"must disable-hybrid-kv-cache-manager" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: gineCore pid=120) ERROR 05-18 01:31:14 [core.py:1108] ValueError: Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type. but if i add --no-disable-hybrid-kv-cache-manager it sa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: vllm0.19.1 with llmcache with qwen3.6-27B-FP8 failed bug ### Your current environment ubuntu22.04 vllm/vllm-openai:v0.19.1 ### 🐛 Describe the bug [Bug]: vllm0.19.1 with llmcache with qwen3.6-27B-FP8 failed (Engin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: vllm0.19.1 with llmcache with qwen3.6-27B-FP8 failed bug ### Your current environment ubuntu22.04 vllm/vllm-openai:v0.19.1 ### 🐛 Describe the bug [Bug]: vllm0.19.1 with llmcache with qwen3.6-27B-FP8 failed (Engin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
