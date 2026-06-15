# vllm-project/vllm#8890: [Bug]: Variance Between Mutiple Prefix Cache Example runs

| 字段 | 值 |
| --- | --- |
| Issue | [#8890](https://github.com/vllm-project/vllm/issues/8890) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Variance Between Mutiple Prefix Cache Example runs

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Ran ```python examples/offline_inference_with_prefix.py``` for multiple times but got variant results of speedup, sometimes it is less than 1. ``` Generated answers are the same: True Speed up of cached generation compared to the regular is: 0.14 ``` ``` Generated answers are the same: True Speed up of cached generation compared to the regular is: 1.05 ``` ``` Generated answers are the same: True Speed up of cached generation compared to the regular is: 0.84 ``` ``` Generated answers are the same: True Speed up of cached generation compared to the regular is: 0.62 ``` Is this an expected variance? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#9077 [Misc] Improved prefix cache example

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #9077 [Misc] Improved prefix cache example...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #9077 [Misc] Improved prefix cache example Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Variance Between Mutiple Prefix Cache Example runs bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Ran ```python examples/offline_inference_with_prefix.py``` for multip...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9077](https://github.com/vllm-project/vllm/pull/9077) | closes_keyword | 0.95 | [Misc] Improved prefix cache example | FIX #8890 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering d |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
