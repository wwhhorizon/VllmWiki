# vllm-project/vllm#23037: [Usage]: cpu infernce with kv-cache on gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#23037](https://github.com/vllm-project/vllm/issues/23037) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: cpu infernce with kv-cache on gpu

### Issue 正文摘录

### Your current environment i found ktransformers and ik_llama have solution for large models don't fit into gpu ram they allow inference in cpu but keep kv-cache in gpu i want have same setup in vllm is this possible ? for example to load large 200B or 671B model on ram and keep kvcache on gpu ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: u ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: u usage;stale ### Your current environment i found ktransformers and ik_llama have solution for large models don't fit into gpu ram they allow inference in cpu but keep kv-cache in gpu i want have same setup in vllm is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: cpu infernce with kv-cache on gpu usage;stale ### Your current environment i found ktransformers and ik_llama have solution for large models don't fit into gpu ram they allow inference in cpu but keep kv-cache...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: cpu infernce with kv-cache on gpu usage;stale ### Your current environment i found ktransformers and ik_llama have solution for large models don't fit into gpu ram they allow inference in cpu but keep kv-cache...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
