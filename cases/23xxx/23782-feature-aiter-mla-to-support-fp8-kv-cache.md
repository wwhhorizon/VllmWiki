# vllm-project/vllm#23782: [Feature]: Aiter MLA to support FP8 KV Cache

| 字段 | 值 |
| --- | --- |
| Issue | [#23782](https://github.com/vllm-project/vllm/issues/23782) |
| 状态 | closed |
| 标签 | performance;feature request;rocm;stale;v1 |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;quantization |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;fp8 |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Aiter MLA to support FP8 KV Cache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - Motivation: - MLA decode performance for DeepSeek, Kimi-k2, etc. - Support higher throughput to KV transfer for P/D disaggregated - Implement vLLM side of logic to work with - https://github.com/ROCm/aiter/issues/899 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Aiter MLA to support FP8 KV Cache performance;feature request;rocm;stale;v1 ### 🚀 The feature, motivation and pitch - Motivation: - MLA decode performance for DeepSeek, Kimi-k2, etc. - Support higher throughp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Aiter MLA to support FP8 KV Cache performance;feature request;rocm;stale;v1 ### 🚀 The feature, motivation and pitch - Motivation: - MLA decode performance for DeepSeek, Kimi-k2, etc. - Support higher throughp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Aiter MLA to support FP8 KV Cache performance;feature request;rocm;stale;v1 ### 🚀 The feature, motivation and pitch - Motivation: - MLA decode performance for DeepSeek, Kimi-k2, etc. - Support higher throughp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: - MLA decode performance for DeepSeek, Kimi-k2, etc. - Support higher throughput to KV transfer for P/D disaggregated - Implement vLLM side of logic to work with - https://github.com/ROCm/aiter/issues/899 ### Alternativ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Aiter MLA to support FP8 KV Cache performance;feature request;rocm;stale;v1 ### 🚀 The feature, motivation and pitch - Motivation: - MLA decode performance for DeepSeek, Kimi-k2, etc. - Support higher throughp...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23783: Should have ROCm label: NO (0 matches) #23782: Should have ROCm label: YES (1 matches) • aiter (substring) in title: 1 matches (searchIn: title) #237 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
