# vllm-project/vllm#14236: [Feature]: Bump xgrammar version to 1.1.14 to support ARM64 processors

| 字段 | 值 |
| --- | --- |
| Issue | [#14236](https://github.com/vllm-project/vllm/issues/14236) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Bump xgrammar version to 1.1.14 to support ARM64 processors

### Issue 正文摘录

### 🚀 The feature, motivation and pitch i noticed that xgrammar only runs on x86, and that there is explicit code in VLLM to fall back on outlines if running on, say, arm64. The latest release (1.1.14) of xgrammar supports arm64. Maybe vllm can bump their version and test on arm64? See: https://github.com/mlc-ai/xgrammar/releases/tag/v0.1.14 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Bump xgrammar version to 1.1.14 to support ARM64 processors feature request;stale ### 🚀 The feature, motivation and pitch i noticed that xgrammar only runs on x86, and that there is explicit code in VLLM to f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: Bump xgrammar version to 1.1.14 to support ARM64 processors feature request;stale ### 🚀 The feature, motivation and pitch i noticed that xgrammar only runs on x86, and that there is explicit code in VLLM to fall ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: code in VLLM to fall back on outlines if running on, say, arm64. The latest release (1.1.14) of xgrammar supports arm64. Maybe vllm can bump their version and test on arm64? See: https://github.com/mlc-ai/xgrammar/relea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
