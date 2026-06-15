# vllm-project/vllm#24050: [Feature]: Cutlass v4.2.0 Support

| 字段 | 值 |
| --- | --- |
| Issue | [#24050](https://github.com/vllm-project/vllm/issues/24050) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Cutlass v4.2.0 Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thor and Spark support Support for Blackwell SM121 kernels for DGX Spark GPUs. Share the major codes with Blackwell SM120 kernels. Support for Blackwell SM100 fp4 gemv kernels. Kernel codes: Gemv kernel. Example codes: example 91 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 🚀 The feature, motivation and pitch Thor and Spark support Support for Blackwell SM121 kernels for DGX Spark GPUs. Share the major codes with Blackwell SM120 kernels. Support for Blackwell SM100 fp4 gemv kernels. Kernel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Cutlass v4.2.0 Support feature request ### 🚀 The feature, motivation and pitch Thor and Spark support Support for Blackwell SM121 kernels for DGX Spark GPUs. Share the major codes with Blackwell SM120 kernels...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: he major codes with Blackwell SM120 kernels. Support for Blackwell SM100 fp4 gemv kernels. Kernel codes: Gemv kernel. Example codes: example 91 ### Alternatives _No response_ ### Additional context _No response_ ### Bef...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Cutlass v4.2.0 Support feature request ### 🚀 The feature, motivation and pitch Thor and Spark support Support for Blackwell SM121 kernels for DGX Spark GPUs. Share the major codes with Blackwell SM120 kernels...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
