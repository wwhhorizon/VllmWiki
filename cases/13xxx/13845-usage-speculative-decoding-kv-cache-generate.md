# vllm-project/vllm#13845: [Usage]: Speculative Decoding KV Cache Generate

| 字段 | 值 |
| --- | --- |
| Issue | [#13845](https://github.com/vllm-project/vllm/issues/13845) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Speculative Decoding KV Cache Generate

### Issue 正文摘录

### Your current environment For speculative inference, suppose the sequence is a, b, c, d, e, and the speculative proposal is f, g, h. It is observed that parallel inference is done by expanding along the batch dimension. In this case, when expanding, the token_ids of the resulting sequence would be a, b, c, d, e, f, g, h for the request. When are the kv caches for tokens f, g, h calculated? And in which code files can I find the related implementation? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Speculative Decoding KV Cache Generate usage;stale ### Your current environment For speculative inference, suppose the sequence is a, b, c, d, e, and the speculative proposal is f, g, h. It is observed that par...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: Speculative Decoding KV Cache Generate usage;stale ### Your current environment For speculative inference, suppose the sequence is a, b, c, d, e, and the speculative proposal is f, g, h. It is observed that par...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
