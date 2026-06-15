# vllm-project/vllm#35612: [Bug]: invalid argument at cumem_allocator.cpp:119

| 字段 | 值 |
| --- | --- |
| Issue | [#35612](https://github.com/vllm-project/vllm/issues/35612) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: invalid argument at cumem_allocator.cpp:119

### Issue 正文摘录

### 🐛 Describe the bug The output of vllm serve "Qwen/Qwen3-4B" --enable-sleep-mode when launch vllm serve "Qwen/Qwen3-4B" --enable-sleep-mode, it response CUDA Error:invalid argument at cumem_allocator.cpp:119, the root cause is cuDeviceGetAttribute is being wrong wrapped by CUDA_CHECK, and it cause the wrong error message. image this is the error message before fix, after the fix code is implemented, it runs normal. image ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#35685 Fix: Suppress spurious cuDeviceGetAttribute errors in cumem_allocator

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: when launch vllm serve "Qwen/Qwen3-4B" --enable-sleep-mode, it response CUDA Error:invalid argument at cumem_allocator.cpp:119, the root cause is cuDeviceGetAttribute is being wrong wrapped by CUDA_CHECK, and it cause t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tor.cpp:119 bug;stale ### 🐛 Describe the bug The output of vllm serve "Qwen/Qwen3-4B" --enable-sleep-mode when launch vllm serve "Qwen/Qwen3-4B" --enable-sleep-mode, it response CUDA Error:invalid argument at cumem_allo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: invalid argument at cumem_allocator.cpp:119 bug;stale ### 🐛 Describe the bug The output of vllm serve "Qwen/Qwen3-4B" --enable-sleep-mode when launch vllm serve "Qwen/Qwen3-4B" --enable-sleep-mode, it response CU...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api cuda #35685 Fix: Suppress spurious cuDeviceGetAttribute erro...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35685](https://github.com/vllm-project/vllm/pull/35685) | closes_keyword | 0.95 | Fix: Suppress spurious cuDeviceGetAttribute errors in cumem_allocator | Fixes #35612 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
