# vllm-project/vllm#29564: [Doc]: Make PyTorch profiler gzip and CUDA time dump configurable

| 字段 | 值 |
| --- | --- |
| Issue | [#29564](https://github.com/vllm-project/vllm/issues/29564) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Make PyTorch profiler gzip and CUDA time dump configurable

### Issue 正文摘录

### 📚 The doc issue We observed that enabling both use_gzip and dump_self_cuda_time_total in the vLLM torch profiler introduces significant overhead during profiling. For example, when profiling 10 randomly generated requests (1000 input tokens, 200 output tokens) on an A100 using the Qwen3-32B model, we found that gzip compression of the profiling trace and dumping the CUDA time table take ~68 seconds, dominating the overall profiling time. The main sources of overhead appear to be: 1. Gzip compression of the profiling trace file 2. Generation and dumping of the CUDA time summary table After disabling these two features, the total profiling dump time is reduced to ~18 seconds. In many profiling scenarios (e.g., quick performance checks or small-scale experiments), users may not need gzip compression or the CUDA time table. Therefore, it would be helpful to make these two behaviors individually configurable via environment variables—enabled by default for completeness, but optionally turnable off when faster profiling turnaround is preferred. Moreover, gzip compression could potentially be performed asynchronously after the trace is dumped, allowing lower-latency profiling in stag...

## 现有链接修复摘要

#29568 [Misc][Profiling] Make PyTorch profiler gzip and CUDA time dump configurable

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Doc]: Make PyTorch profiler gzip and CUDA time dump configurable documentation ### 📚 The doc issue We observed that enabling both use_gzip and dump_self_cuda_time_total in the vLLM torch profiler introduces significant...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Doc]: Make PyTorch profiler gzip and CUDA time dump configurable documentation ### 📚 The doc issue We observed that enabling both use_gzip and dump_self_cuda_time_total in the vLLM torch profiler introduces significant...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Doc]: Make PyTorch profiler gzip and CUDA time dump configurable documentation ### 📚 The doc issue We observed that enabling both use_gzip and dump_self_cuda_time_total in the vLLM torch profiler introduces significant...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: frequently asked questions. performance model_support cuda slowdown env_dependency #29568 [Misc][Profiling] Make PyTorch profiler gzip and CUDA time dump configurable 📚 The doc issue
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s. In many profiling scenarios (e.g., quick performance checks or small-scale experiments), users may not need gzip compression or the CUDA time table. Therefore, it would be helpful to make these two behaviors individu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29568](https://github.com/vllm-project/vllm/pull/29568) | closes_keyword | 0.95 | [Misc][Profiling] Make PyTorch profiler gzip and CUDA time dump configurable | Fixes #29564 ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The purpose of the PR, such as "Fi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
