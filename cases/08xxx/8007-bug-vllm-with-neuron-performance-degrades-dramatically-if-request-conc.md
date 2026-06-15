# vllm-project/vllm#8007: [Bug]: vLLM with Neuron performance degrades dramatically if request concurrency is >= max_num_seqs

| 字段 | 值 |
| --- | --- |
| Issue | [#8007](https://github.com/vllm-project/vllm/issues/8007) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM with Neuron performance degrades dramatically if request concurrency is >= max_num_seqs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When vLLM is used with Neuron, as long as number of concurrent requests are less than `max_num_seqs`, performance is nominal, but if number of concurrent requests is `>= max_num_seqs`, performance degrades dramatically. For example, in one test with `max_num_seqs=4`, request latency for up to `3` concurrent requests is in the 20 second range, but with `4` concurrent requests, it jumps to over 500 seconds. Logs show continual preemption, even when `gpu_memory_utilization = 0.9`. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#8008 Neuron cache blocks must be 1 more than max num seqs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vLLM with Neuron performance degrades dramatically if request concurrency is >= max_num_seqs bug;stale ### Your current environment ### 🐛 Describe the bug When vLLM is used with Neuron, as long as number of concu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 9`. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: >= max_num_seqs`, performance degrades dramatically. For example, in one test with `max_num_seqs=4`, request latency for up to `3` concurrent requests is in the 20 second range, but with `4` concurrent requests, it jump...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;import_error;nan_inf;slowdown env_dependency #8008 Neuron cache blocks must be 1 more than max num seqs Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8008](https://github.com/vllm-project/vllm/pull/8008) | closes_keyword | 0.95 | Neuron cache blocks must be 1 more than max num seqs | FIX #8007 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- insid |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
