# vllm-project/vllm#18240: [Bug]: `RuntimeError: !stack.empty() INTERNAL ASSERT FAILED` in PyTorch when stopping vLLM profiler

| 字段 | 值 |
| --- | --- |
| Issue | [#18240](https://github.com/vllm-project/vllm/issues/18240) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `RuntimeError: !stack.empty() INTERNAL ASSERT FAILED` in PyTorch when stopping vLLM profiler

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was trying to benchmarking vLLM server like following [this page](https://docs.vllm.ai/en/latest/contributing/profiling/profiling_index.html#openai-server). - Related issue: https://github.com/pytorch/pytorch/issues/101632 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: or: !stack.empty() INTERNAL ASSERT FAILED` in PyTorch when stopping vLLM profiler bug;stale ### Your current environment ### 🐛 Describe the bug I was trying to benchmarking vLLM server like following [this page](https:/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;operato...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: pty() INTERNAL ASSERT FAILED` in PyTorch when stopping vLLM profiler bug;stale ### Your current environment ### 🐛 Describe the bug I was trying to benchmarking vLLM server like following [this page](https://docs.vllm.ai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ogits;scheduler_memory;speculative_decoding cache;cuda;operator;sampling;triton build_error;crash;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
