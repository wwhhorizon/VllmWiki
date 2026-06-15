# vllm-project/vllm#9230: [Bug]: Qwen2.5-72B-Instruct压测出现AsyncLLMEngine has failed, terminating server process

| 字段 | 值 |
| --- | --- |
| Issue | [#9230](https://github.com/vllm-project/vllm/issues/9230) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-72B-Instruct压测出现AsyncLLMEngine has failed, terminating server process

### Issue 正文摘录

### Your current environment ### Model Input Dumps None ### 🐛 Describe the bug 如有其他信息可向我咨询 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen2.5-72B-Instruct压测出现AsyncLLMEngine has failed, terminating server process bug;stale ### Your current environment ### Model Input Dumps None ### 🐛 Describe the bug 如有其他信息可向我咨询 ### Before submitting a new issue
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 我咨询 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: allel;frontend_api;model_support cuda;kernel crash env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size Your current environment
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nt distributed_parallel;frontend_api;model_support cuda;kernel crash env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | function> + 0x7ea5 (0x7f8622784ea5 in /lib64/libpthread.so.0) frame #4: clone + 0x6d (0x7f8621da4b0d in /lib64/libc.so.6) ``` </details> ### model input dumps none ### 🐛 d |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | function> + 0x7ea5 (0x7f8622784ea5 in /lib64/libpthread.so.0) frame #6: clone + 0x6d (0x7f8621da4b0d in /lib64/libc.so.6) exception raised from ncclcommwatchdog at ../torch/csrc |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
