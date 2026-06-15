# vllm-project/vllm#6576: Fp8 support for mi300x

| 字段 | 值 |
| --- | --- |
| Issue | [#6576](https://github.com/vllm-project/vllm/issues/6576) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Fp8 support for mi300x

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It was not clear for me if the fp8 support is available for rocm. But I got with 5.2 : fp8 quantization is currently not supported in ROCm. There are plans to have it available? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Fp8 support for mi300x feature request;rocm ### 🚀 The feature, motivation and pitch It was not clear for me if the fp8 support is available for rocm. But I got with 5.2 : fp8 quantization is currently not supported in R...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Fp8 support for mi300x feature request;rocm ### 🚀 The feature, motivation and pitch It was not clear for me if the fp8 support is available for rocm. But I got with 5.2 : fp8 quantization is currently not supported in
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Fp8 support for mi300x feature request;rocm ### 🚀 The feature, motivation and pitch It was not clear for me if the fp8 support is available for rocm. But I got with 5.2 : fp8 quantization is currently not supported in R...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
