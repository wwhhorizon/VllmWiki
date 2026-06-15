# vllm-project/vllm#6059: [Bug][CI/Build]: Missing attribute 'nvmlDeviceGetHandleByIndex' in AMD tests

| 字段 | 值 |
| --- | --- |
| Issue | [#6059](https://github.com/vllm-project/vllm/issues/6059) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][CI/Build]: Missing attribute 'nvmlDeviceGetHandleByIndex' in AMD tests

### Issue 正文摘录

### Your current environment AMD CI ### 🐛 Describe the bug Most AMD CI runs are failing. Example: https://buildkite.com/vllm/ci-aws/builds/3706#0190716d-09a9-49d5-a9d3-f61dc45ae12c

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug][CI/Build]: Missing attribute 'nvmlDeviceGetHandleByIndex' in AMD tests bug;rocm ### Your current environment AMD CI ### 🐛 Describe the bug Most AMD CI runs are failing. Example: https://buildkite.com/vllm/ci-aws/b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /Build]: Missing attribute 'nvmlDeviceGetHandleByIndex' in AMD tests bug;rocm ### Your current environment AMD CI ### 🐛 Describe the bug Most AMD CI runs are failing. Example: https://buildkite.com/vllm/ci-aws/builds/37...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug][CI/Build]: Missing attribute 'nvmlDeviceGetHandleByIndex' in AMD tests bug;rocm ### Your current environment AMD CI ### 🐛 Describe the bug Most AMD CI runs are failing. Example: https://buildkite.com/vllm/ci-aws/b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
