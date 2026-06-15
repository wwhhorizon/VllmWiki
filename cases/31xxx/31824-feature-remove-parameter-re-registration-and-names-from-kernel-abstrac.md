# vllm-project/vllm#31824: [Feature]: Remove parameter re-registration and names from kernel abstraction

| 字段 | 值 |
| --- | --- |
| Issue | [#31824](https://github.com/vllm-project/vllm/issues/31824) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Remove parameter re-registration and names from kernel abstraction

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In ScaledMMLinearKernel, each quantization type has different names for parameters (weights and scales), which have to be passed to the kernel as strings so that the kernel can access them indirectly. We also do some param re-registration. However, I think with torch 2.8+, we should be able to use torch parameter subclasses normally, without reregistration. Previous discussion here: https://vllm-dev.slack.com/archives/C07RFT1DVT2/p1755704356536069 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: help wanted;feature request ### 🚀 The feature, motivation and pitch In ScaledMMLinearKernel, each quantization type has different names for parameters (weights and scales), which have to be passed to the kernel as strin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: out reregistration. Previous discussion here: https://vllm-dev.slack.com/archives/C07RFT1DVT2/p1755704356536069 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: er re-registration and names from kernel abstraction help wanted;feature request ### 🚀 The feature, motivation and pitch In ScaledMMLinearKernel, each quantization type has different names for parameters (weights and sc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
