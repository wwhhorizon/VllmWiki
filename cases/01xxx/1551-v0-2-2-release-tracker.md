# vllm-project/vllm#1551: [v0.2.2] Release Tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#1551](https://github.com/vllm-project/vllm/issues/1551) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [v0.2.2] Release Tracker

### Issue 正文摘录

**ETA**: ~~Nov 3rd (Fri) - Nov 6th (Mon).~~ Nov 17th (Fri) - 19th (Sun). ## Major changes * Extensive refactoring for better tensor parallelism & quantization support * Changes in scheduler: from 1D flattened input tensor to 2D tensor * Bump up to PyTorch v2.1 + CUDA 12.1 * New models: Yi, ChatGLM, Phi * Added LogitsProcessor API * Preliminary support for SqueezeLLM ## PRs to be merged before the release - [x] CUDA 12 #1527 - [x] Yarn #1264, #1161 - [x] Phi model #1664 - ~~[ ] Support embedding inputs #1265~~

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ). ## Major changes * Extensive refactoring for better tensor parallelism & quantization support * Changes in scheduler: from 1D flattened input tensor to 2D tensor * Bump up to PyTorch v2.1 + CUDA 12.1 * New models: Yi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: # Major changes * Extensive refactoring for better tensor parallelism & quantization support * Changes in scheduler: from 1D flattened input tensor to 2D tensor * Bump up to PyTorch v2.1 + CUDA 12.1 * New models: Yi, Ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed input tensor to 2D tensor * Bump up to PyTorch v2.1 + CUDA 12.1 * New models: Yi, ChatGLM, Phi * Added LogitsProcessor API * Preliminary support for SqueezeLLM ## PRs to be merged before the release - [x] CUDA 12 #15...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: toring for better tensor parallelism & quantization support * Changes in scheduler: from 1D flattened input tensor to 2D tensor * Bump up to PyTorch v2.1 + CUDA 12.1 * New models: Yi, ChatGLM, Phi * Added LogitsProcesso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
