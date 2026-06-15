# vllm-project/vllm#10890: [BUG] [MultiStep+AsyncOutputProc] the remaining steps not released when request output reaches max-token

| 字段 | 值 |
| --- | --- |
| Issue | [#10890](https://github.com/vllm-project/vllm/issues/10890) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUG] [MultiStep+AsyncOutputProc] the remaining steps not released when request output reaches max-token

### Issue 正文摘录

### Your current environment OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.11.7 | packaged by conda-forge | (main, Dec 15 2023, 08:38:37) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-6.8.0-45-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using: --num-scheduler-steps 20 Sending a request with SamplingParams : max_tokens=4 Engine will stop the request at step 4, but remaining 16 steps are suspended，When the next request comes，the remaining 16 steps of the previous request will continue execute. The Latency of the first token of a new request will be increased. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: g;stale ### Your current environment OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python vers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [BUG] [MultiStep+AsyncOutputProc] the remaining steps not released when request output reaches max-token bug;stale ### Your current environment OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: untime) Python platform: Linux-6.8.0-45-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using: --num-scheduler-steps 20 Sen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e remaining 16 steps of the previous request will continue execute. The Latency of the first token of a new request will be increased. ### Before submitting a new issue... - [X] Make sure you already searched for releva...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: th-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using: --num-scheduler-steps 20 Sending a request with SamplingParams : max_tokens=4 Engine...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
