# vllm-project/vllm#3931: [Usage]: How to offload some layers to CPU？

| 字段 | 值 |
| --- | --- |
| Issue | [#3931](https://github.com/vllm-project/vllm/issues/3931) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to offload some layers to CPU？

### Issue 正文摘录

### Your current environment None ### How would you like to use vllm I want to load qwen2-14B-chat using VLLM, but I only have 1 RTX4090(24G). Can vllm offload some layers to cpu and others to gpu? As I know, the transformers-accelerate and llama.cpp can do it. But I want to use the multilora switch function in VLLM.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt environment None ### How would you like to use vllm I want to load qwen2-14B-chat using VLLM, but I only have 1 RTX4090(24G). Can vllm offload some layers to cpu and others to gpu? As I know, the transformers-acceler...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to use vllm I want to load qwen2-14B-chat using VLLM, but I only have 1 RTX4090(24G). Can vllm offload some layers to cpu and others to gpu? As I know, the transformers-accelerate and llama.cpp can do it. But I want to...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: How to offload some layers to CPU？ usage;stale ### Your current environment None ### How would you like to use vllm I want to load qwen2-14B-chat using VLLM, but I only have 1 RTX4090(24G). Can vllm offload som...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to offload some layers to CPU？ usage;stale ### Your current environment None ### How would you like to use vllm I want to load qwen2-14B-chat using VLLM, but I only have 1 RTX4090(24G). Can vllm offload som...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
