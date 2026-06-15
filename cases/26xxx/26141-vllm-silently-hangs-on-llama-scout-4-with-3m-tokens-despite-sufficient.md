# vllm-project/vllm#26141: vLLM silently hangs on LLaMA Scout 4 with >3M tokens despite sufficient GPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#26141](https://github.com/vllm-project/vllm/issues/26141) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM silently hangs on LLaMA Scout 4 with >3M tokens despite sufficient GPU memory

### Issue 正文摘录

### Name of failing test LLM chat ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test *Description:** vLLM silently hangs when processing more than ~3 million tokens on LLaMA 4 Scout, despite sufficient GPU memory. No error logs are generated, even with full debugging enabled. **Environment:** - Model: LLaMA 4 Scout - GPUs: 8 × NVIDIA H100 - VRAM: ~15M tokens capacity - Model Context Size: 10M tokens - vLLM Version: 10.2 - OS: Ubuntu 24.04 - NVIDIA Driver: 580 - CUDA: 12.9 **Debugging:** ```bash os.environ["VLLM_TRACE_FUNCTION"] = "1" os.environ["CUDA_LAUNCH_BLOCKING"] = "1" os.environ["VLLM_LOGGING_LEVEL"] = "DEBUG" os.environ["NCCL_DEBUG"] = "TRACE" Observed Behavior: Process hangs silently beyond ~3M tokens. CPU/GPU profiling shows: %Own %Total OwnTime TotalTime Function 0.00% 0.00% 468.8s 468.8s sched_yield (vllm/distributed/utils.py) 0.00% 0.00% 86.35s 102.4s get_metadata (vllm/distributed/device_communication.py) 0.00% 0.00% 52.41s 655.6s acquire_read (vllm/distributed/device_communication.py) Appears stuck in sched_yield / acquire_read, suggesting a potential distr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vLLM silently hangs on LLaMA Scout 4 with >3M tokens despite sufficient GPU memory stale;ci-failure ### Name of failing test LLM chat ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by ex...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vLLM silently hangs on LLaMA Scout 4 with >3M tokens despite sufficient GPU memory stale;ci-failure ### Name of failing test LLM chat ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tly hangs on LLaMA Scout 4 with >3M tokens despite sufficient GPU memory stale;ci-failure ### Name of failing test LLM chat ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external lib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: enabled. **Environment:** - Model: LLaMA 4 Scout - GPUs: 8 × NVIDIA H100 - VRAM: ~15M tokens capacity - Model Context Size: 10M tokens - vLLM Version: 10.2 - OS: Ubuntu 24.04 - NVIDIA Driver: 580 - CUDA: 12.9 **Debuggin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ```bash os.environ["VLLM_TRACE_FUNCTION"] = "1" os.environ["CUDA_LAUNCH_BLOCKING"] = "1" os.environ["VLLM_LOGGING_LEVEL"] = "DEBUG" os.environ["NCCL_DEBUG"] = "TRACE" Observed Behavior: Process hangs silently beyond ~3M...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
