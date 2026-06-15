# vllm-project/vllm#6030: [Bug]: identical branches in csrc/quantization/marlin/sparse/marlin_24_cuda_kernel.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#6030](https://github.com/vllm-project/vllm/issues/6030) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: identical branches in csrc/quantization/marlin/sparse/marlin_24_cuda_kernel.cu

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug At https://github.com/vllm-project/vllm/blob/main/csrc/quantization/marlin/sparse/marlin_24_cuda_kernel.cu#L296 there is an if statement with an else. Both branches are the same. The comment preceding it leads me to believe they were intended to be very different. IOW, this looks like a copy and paste without updating one or the other. I don't know the theory to suggest a fix. But I can just say this looks suspicious.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n't know the theory to suggest a fix. But I can just say this looks suspicious.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: identical branches in csrc/quantization/marlin/sparse/marlin_24_cuda_kernel.cu bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug At https://github.com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: identical branches in csrc/quantization/marlin/sparse/marlin_24_cuda_kernel.cu bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug At https://github.com...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sparse/marlin_24_cuda_kernel.cu#L296 there is an if statement with an else. Both branches are the same. The comment preceding it leads me to believe they were intended to be very different. IOW, this looks like a copy a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: branches in csrc/quantization/marlin/sparse/marlin_24_cuda_kernel.cu bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug At https://github.com/vllm-project/vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
