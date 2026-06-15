# vllm-project/vllm#17843: [Usage]: Inquiry About AMD APU Support (e.g., AMD AI Max+ 395) and Handling in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#17843](https://github.com/vllm-project/vllm/issues/17843) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Inquiry About AMD APU Support (e.g., AMD AI Max+ 395) and Handling in vLLM

### Issue 正文摘录

### Your current environment I am interested in using vLLM for inference on systems equipped with AMD APUs, such as the AMD AI Max+ 395, which integrates both CPU and GPU capabilities along with an NPU. I would like to know if vLLM currently supports AMD APUs for LLM inference and, if so, how these APUs are treated within the vLLM framework: **Support**: Does vLLM have support for AMD APUs, specifically models like the AMD AI Max+ 395? Are there any specific configurations or prerequisites required to enable this support? **Handling**: If supported, are AMD APUs treated as GPUs (leveraging ROCm for the integrated GPU) or as CPUs (using CPU-based inference)? Alternatively, is there support for utilizing the NPU component of these APUs?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: amework: **Support**: Does vLLM have support for AMD APUs, specifically models like the AMD AI Max+ 395? Are there any specific configurations or prerequisites required to enable this support? **Handling**: If supported...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he vLLM framework: **Support**: Does vLLM have support for AMD APUs, specifically models like the AMD AI Max+ 395? Are there any specific configurations or prerequisites required to enable this support? **Handling**: If...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rt? **Handling**: If supported, are AMD APUs treated as GPUs (leveraging ROCm for the integrated GPU) or as CPUs (using CPU-based inference)? Alternatively, is there support for utilizing the NPU component of these APUs?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: About AMD APU Support (e.g., AMD AI Max+ 395) and Handling in vLLM usage;stale ### Your current environment I am interested in using vLLM for inference on systems equipped with AMD APUs, such as the AMD AI Max+ 395, whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
