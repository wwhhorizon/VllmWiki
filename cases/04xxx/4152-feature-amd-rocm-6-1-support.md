# vllm-project/vllm#4152: [Feature]:  AMD ROCm 6.1 Support

| 字段 | 值 |
| --- | --- |
| Issue | [#4152](https://github.com/vllm-project/vllm/issues/4152) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  AMD ROCm 6.1 Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [AMD ROCm 6.1](https://github.com/ROCm/ROCm/releases/tag/rocm-6.1.0) has been released with significant performance improvements for AMD GPUs, including the MI300X.. When can we expect support for ROCm 6.1 on vLLM? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: AMD ROCm 6.1 Support feature request;rocm ### 🚀 The feature, motivation and pitch [AMD ROCm 6.1](https://github.com/ROCm/ROCm/releases/tag/rocm-6.1.0) has been released with significant performance improvemen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: AMD ROCm 6.1 Support feature request;rocm ### 🚀 The feature, motivation and pitch [AMD ROCm 6.1](https://github.com/ROCm/ROCm/releases/tag/rocm-6.1.0) has been released with significant performance improvemen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
