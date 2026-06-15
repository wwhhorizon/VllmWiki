# vllm-project/vllm#17325: [Feature]: Integrate FlashInfer Blackwell kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#17325](https://github.com/vllm-project/vllm/issues/17325) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate FlashInfer Blackwell kernels

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have manually verified that https://github.com/flashinfer-ai/flashinfer/pull/1039 gives correctness, so we will want to upgrade to the next version of flashinfer once the above PR lands. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Integrate FlashInfer Blackwell kernels feature request ### 🚀 The feature, motivation and pitch We have manually verified that https://github.com/flashinfer-ai/flashinfer/pull/1039 gives correctness, so we wil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Integrate FlashInfer Blackwell kernels feature request ### 🚀 The feature, motivation and pitch We have manually verified that https://github.com/flashinfer-ai/flashinfer/pull/1039 gives correctness, so we wil...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nfer/pull/1039 gives correctness, so we will want to upgrade to the next version of flashinfer once the above PR lands. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new iss...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Integrate FlashInfer Blackwell kernels feature request ### 🚀 The feature, motivation and pitch We have manually verified that https://github.com/flashinfer-ai/flashinfer/pull/1039 gives correctness, so we wil...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
